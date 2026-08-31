import sys
import numpy as np
import pandas as pd
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QLabel, QTableWidget, QTableWidgetItem, QTabWidget,
    QFileDialog, QGroupBox, QHeaderView, QDoubleSpinBox, QSplitter,
    QTextEdit, QFormLayout, QMessageBox, QProgressBar
)
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

# PDF Generation Imports
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors


class CyclingKinematicsEngine:
    """Models 360-degree pedal cycle kinetics, power distribution, and dynamic rider performance."""

    @classmethod
    def simulate_pedal_cycle(cls, rider_mass=70.0, cadence=90.0, crank_length_mm=172.5,
                              gear_ratio=3.5, max_pedal_force_n=400.0, lr_balance_pct=52.0,
                              resistance_coef=0.005, resolution=360):
        """
        Simulates force vectors across 0-360 degrees crank angle.
        Peak tangential force occurs around 90° (downstroke) and 270° (left downstroke).
        """
        angles_deg = np.linspace(0, 360, resolution)
        angles_rad = np.radians(angles_deg)
        crank_length_m = crank_length_mm / 1000.0
        angular_vel_rad_s = (cadence * 2 * np.pi) / 60.0

        # Left / Right Split Dynamics
        left_ratio = lr_balance_pct / 100.0
        right_ratio = 1.0 - left_ratio

        # Tangential (Effective Propulsive Force) vs Radial (Ineffective Force) Models
        # Right Downstroke Peak at 90°, Left Downstroke Peak at 270°
        tangential_right = max_pedal_force_n * right_ratio * np.maximum(0, np.sin(angles_rad)) ** 2
        tangential_left = max_pedal_force_n * left_ratio * np.maximum(0, np.sin(angles_rad - np.pi)) ** 2
        net_tangential_force = tangential_right + tangential_left

        # Ineffective Radial Force (pushing along crank arms, waste energy)
        radial_force = 0.25 * max_pedal_force_n * np.abs(np.cos(angles_rad))
        total_applied_force = np.sqrt(net_tangential_force ** 2 + radial_force ** 2)

        # Torque (N·m) = Tangential Force * Crank Arm Length
        torque = net_tangential_force * crank_length_m

        # Instantaneous Power (Watts) = Torque * Angular Velocity
        inst_power = torque * angular_vel_rad_s

        df = pd.DataFrame({
            "Crank_Angle_Deg": angles_deg,
            "Tangential_Force_N": net_tangential_force,
            "Total_Applied_Force_N": total_applied_force,
            "Torque_Nm": torque,
            "Power_Watts": inst_power,
            "Right_Leg_Force_N": tangential_right,
            "Left_Leg_Force_N": tangential_left
        })

        return df

    @classmethod
    def calculate_cycle_metrics(cls, df, lr_balance_pct):
        avg_power = float(np.mean(df["Power_Watts"]))
        peak_power = float(np.max(df["Power_Watts"]))
        avg_torque = float(np.mean(df["Torque_Nm"]))
        peak_torque = float(np.max(df["Torque_Nm"]))

        # Pedal Force Efficiency = Tangential Force Work / Total Applied Force Work
        tangential_work = np.sum(df["Tangential_Force_N"])
        total_work = np.sum(df["Total_Applied_Force_N"])
        pedal_efficiency = (tangential_work / max(1.0, total_work)) * 100.0

        metrics = {
            "Average Power": f"{avg_power:.1f} W",
            "Peak Power": f"{peak_power:.1f} W",
            "Average Torque": f"{avg_torque:.1f} N·m",
            "Peak Torque": f"{peak_torque:.1f} N·m",
            "L/R Power Balance": f"{lr_balance_pct:.1f}% L / {100.0 - lr_balance_pct:.1f}% R",
            "Pedal Force Efficiency": f"{pedal_efficiency:.1f}%"
        }

        raw = {
            "avg_power": avg_power,
            "peak_power": peak_power,
            "avg_torque": avg_torque,
            "peak_torque": peak_torque,
            "pedal_efficiency": pedal_efficiency
        }

        return metrics, raw

    @classmethod
    def simulate_distance_course(cls, distance_km=10.0, avg_power_w=250.0,
                                  rider_mass=70.0, bike_mass=8.0, cdA=0.32, elevation_gain_m=100.0):
        """Simulates rider speed, aerodynamic drag, rolling resistance, and completion time."""
        total_mass = rider_mass + bike_mass
        rho = 1.225  # Air density kg/m^3
        cr = 0.004   # Rolling resistance coefficient
        g = 9.81

        distance_m = distance_km * 1000.0
        slope_rad = np.arcsin(min(1.0, elevation_gain_m / max(1.0, distance_m)))

        # Solve for Equilibrium Velocity: Power = (F_drag + F_roll + F_gravity) * V
        # 0.5 * rho * cdA * V^3 + (cr * total_mass * g + total_mass * g * sin(slope)) * V - Power = 0
        a = 0.5 * rho * cdA
        c = (cr * total_mass * g * np.cos(slope_rad)) + (total_mass * g * np.sin(slope_rad))
        
        # Iterative Newton-Raphson solver for velocity
        v = 8.0  # Initial guess m/s
        for _ in range(20):
            f_val = a * (v ** 3) + c * v - avg_power_w
            f_prime = 3 * a * (v ** 2) + c
            v = v - f_val / f_prime

        velocity_mps = max(1.0, v)
        velocity_kmh = velocity_mps * 3.6
        completion_time_sec = distance_m / velocity_mps
        time_minutes = completion_time_sec / 60.0

        # Energy expenditure
        energy_kj = (avg_power_w * completion_time_sec) / 1000.0

        return {
            "distance_km": distance_km,
            "avg_speed_kmh": velocity_kmh,
            "time_minutes": time_minutes,
            "energy_kj": energy_kj,
            "aero_drag_w": 0.5 * rho * cdA * (velocity_mps ** 3),
            "rolling_grav_w": c * velocity_mps
        }


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cycling Biomechanics Simulator")
        self.setGeometry(50, 50, 1450, 920)

        self.cycle_data = {}
        self.course_data = {}

        self.init_ui()
        self.run_simulation()

    def init_ui(self):
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        main_layout = QHBoxLayout(main_widget)

        # Left Sidebar: Inputs & Controls
        sidebar = QGroupBox("Rider & Bike Parameters")
        sidebar_layout = QVBoxLayout(sidebar)

        self.form_layout = QFormLayout()

        self.spn_mass = QDoubleSpinBox(); self.spn_mass.setRange(40, 140); self.spn_mass.setValue(72.0)
        self.spn_cadence = QDoubleSpinBox(); self.spn_cadence.setRange(30, 180); self.spn_cadence.setValue(90.0)
        self.spn_crank = QDoubleSpinBox(); self.spn_crank.setRange(150, 190); self.spn_crank.setValue(172.5); self.spn_crank.setSingleStep(2.5)
        self.spn_gear = QDoubleSpinBox(); self.spn_gear.setRange(1.0, 6.0); self.spn_gear.setValue(3.45); self.spn_gear.setSingleStep(0.1)
        self.spn_force = QDoubleSpinBox(); self.spn_force.setRange(50, 1200); self.spn_force.setValue(420.0)
        self.spn_balance = QDoubleSpinBox(); self.spn_balance.setRange(30, 70); self.spn_balance.setValue(52.0); self.spn_balance.setSingleStep(0.5)
        self.spn_distance = QDoubleSpinBox(); self.spn_distance.setRange(1, 180); self.spn_distance.setValue(20.0)

        self.form_layout.addRow("Rider Mass (kg):", self.spn_mass)
        self.form_layout.addRow("Cadence (RPM):", self.spn_cadence)
        self.form_layout.addRow("Crank Length (mm):", self.spn_crank)
        self.form_layout.addRow("Gear Ratio:", self.spn_gear)
        self.form_layout.addRow("Peak Pedal Force (N):", self.spn_force)
        self.form_layout.addRow("L/R Balance (% Left):", self.spn_balance)
        self.form_layout.addRow("Course Distance (km):", self.spn_distance)

        sidebar_layout.addLayout(self.form_layout)

        self.btn_recalculate = QPushButton("Simulate Revolution & Course")
        self.btn_recalculate.setStyleSheet("background-color: #2E7D32; color: white; font-weight: bold; padding: 8px;")
        self.btn_recalculate.clicked.connect(self.run_simulation)
        sidebar_layout.addWidget(self.btn_recalculate)

        # Data Export Box
        export_box = QGroupBox("Export Options")
        export_layout = QVBoxLayout(export_box)
        self.btn_export_csv = QPushButton("Export Cycle Kinematics (CSV)")
        self.btn_export_csv.clicked.connect(self.export_csv)
        self.btn_export_pdf = QPushButton("Export Performance Report (PDF)")
        self.btn_export_pdf.clicked.connect(self.export_pdf)
        export_layout.addWidget(self.btn_export_csv)
        export_layout.addWidget(self.btn_export_pdf)
        sidebar_layout.addWidget(export_box)

        sidebar_layout.addStretch()
        main_layout.addWidget(sidebar, stretch=1)

        # Right Splitter Layout (Plots & Tables)
        splitter = QSplitter(Qt.Horizontal)

        # Left Column: Graphs Panel
        graph_widget = QWidget()
        graph_layout = QVBoxLayout(graph_widget)
        self.fig_pedal = Figure(figsize=(7, 8))
        self.canvas_pedal = FigureCanvas(self.fig_pedal)
        graph_layout.addWidget(self.canvas_pedal)
        splitter.addWidget(graph_widget)

        # Right Column: Dashboard Panel
        dashboard_widget = QWidget()
        dash_layout = QVBoxLayout(dashboard_widget)
        self.tabs_dashboard = QTabWidget()

        # Tab 1: Pedal Cycle Kinematics Table
        tab_metrics = QWidget()
        layout_metrics = QVBoxLayout(tab_metrics)
        self.table_metrics = QTableWidget()
        layout_metrics.addWidget(self.table_metrics)
        self.tabs_dashboard.addTab(tab_metrics, "Pedal Cycle Kinetics")

        # Tab 2: Distance Performance Simulation Summary
        tab_course = QWidget()
        layout_course = QVBoxLayout(tab_course)
        self.txt_course_summary = QTextEdit()
        self.txt_course_summary.setReadOnly(True)
        self.txt_course_summary.setStyleSheet("font-size: 13px; line-height: 1.4; padding: 10px;")
        layout_course.addWidget(self.txt_course_summary)
        self.tabs_dashboard.addTab(tab_course, "Distance Performance Simulation")

        dash_layout.addWidget(self.tabs_dashboard)
        splitter.addWidget(dashboard_widget)

        splitter.setSizes([800, 500])
        main_layout.addWidget(splitter, stretch=3)

    def run_simulation(self):
        # 1. Simulate 360-degree Pedal Revolution Dynamics
        df_cycle = CyclingKinematicsEngine.simulate_pedal_cycle(
            rider_mass=self.spn_mass.value(),
            cadence=self.spn_cadence.value(),
            crank_length_mm=self.spn_crank.value(),
            gear_ratio=self.spn_gear.value(),
            max_pedal_force_n=self.spn_force.value(),
            lr_balance_pct=self.spn_balance.value()
        )
        metrics, raw_metrics = CyclingKinematicsEngine.calculate_cycle_metrics(df_cycle, self.spn_balance.value())
        self.cycle_data = {"df": df_cycle, "metrics": metrics, "raw": raw_metrics}

        # 2. Simulate Rider Performance over Course Distance
        course = CyclingKinematicsEngine.simulate_distance_course(
            distance_km=self.spn_distance.value(),
            avg_power_w=raw_metrics["avg_power"],
            rider_mass=self.spn_mass.value()
        )
        self.course_data = course

        # 3. Update Visualizations & Tables
        self.plot_biomechanics()
        self.update_metrics_table()
        self.update_course_summary()

    def plot_biomechanics(self):
        self.fig_pedal.clear()
        df = self.cycle_data["df"]

        # Subplot 1: Tangential & Total Pedal Force vs Crank Angle
        ax1 = self.fig_pedal.add_subplot(311)
        ax1.plot(df["Crank_Angle_Deg"], df["Tangential_Force_N"], 'g-', lw=2, label="Effective Tangential Force")
        ax1.plot(df["Crank_Angle_Deg"], df["Total_Applied_Force_N"], 'k--', lw=1.5, alpha=0.7, label="Total Applied Force")
        ax1.set_title("Pedal Force vs Crank Angle (0–360°)")
        ax1.set_ylabel("Force (N)")
        ax1.grid(True, alpha=0.3)
        ax1.legend(loc="upper right", fontsize=8)

        # Subplot 2: Torque & Instantaneous Power Profile
        ax2 = self.fig_pedal.add_subplot(312)
        ax2.plot(df["Crank_Angle_Deg"], df["Power_Watts"], 'b-', lw=2, label="Instantaneous Power (W)")
        ax2.set_ylabel("Power (W)", color='b')
        ax2.tick_params(axis='y', labelcolor='b')

        ax2_sub = ax2.twinx()
        ax2_sub.plot(df["Crank_Angle_Deg"], df["Torque_Nm"], 'r:', lw=1.8, label="Torque (N·m)")
        ax2_sub.set_ylabel("Torque (N·m)", color='r')
        ax2_sub.tick_params(axis='y', labelcolor='r')
        ax2.set_title("Power & Torque Trajectory")
        ax2.grid(True, alpha=0.3)

        # Subplot 3: Left vs Right Leg Force Distribution
        ax3 = self.fig_pedal.add_subplot(313)
        ax3.plot(df["Crank_Angle_Deg"], df["Left_Leg_Force_N"], color='#1976D2', lw=2, label="Left Leg Propulsion")
        ax3.plot(df["Crank_Angle_Deg"], df["Right_Leg_Force_N"], color='#D32F2F', lw=2, label="Right Leg Propulsion")
        ax3.set_title("Left/Right Asymmetry Analysis")
        ax3.set_xlabel("Crank Angle (°)")
        ax3.set_ylabel("Propulsive Force (N)")
        ax3.grid(True, alpha=0.3)
        ax3.legend(loc="upper right", fontsize=8)

        self.fig_pedal.tight_layout()
        self.canvas_pedal.draw()

    def update_metrics_table(self):
        self.table_metrics.clear()
        metrics = self.cycle_data["metrics"]

        self.table_metrics.setRowCount(len(metrics))
        self.table_metrics.setColumnCount(2)
        self.table_metrics.setHorizontalHeaderLabels(["Kinematic / Kinetic Parameter", "Measured Value"])

        for i, (key, value) in enumerate(metrics.items()):
            self.table_metrics.setItem(i, 0, QTableWidgetItem(key))
            self.table_metrics.setItem(i, 1, QTableWidgetItem(value))

        self.table_metrics.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def update_course_summary(self):
        c = self.course_data
        raw = self.cycle_data["raw"]

        html = f"<h2>Rider Distance Simulation ({c['distance_km']:.1f} km)</h2>"
        html += f"<p>Simulated rider output sustained at average mechanical power of <b>{raw['avg_power']:.1f} Watts</b>:</p>"

        html += "<ul>"
        html += f"<li><b>Estimated Completion Time:</b> {c['time_minutes']:.2f} minutes</li>"
        html += f"<li><b>Average Speed:</b> {c['avg_speed_kmh']:.1f} km/h</li>"
        html += f"<li><b>Energy Expenditure:</b> {c['energy_kj']:.1f} kJ</li>"
        html += f"<li><b>Aerodynamic Power Loss:</b> {c['aero_drag_w']:.1f} W ({(c['aero_drag_w']/raw['avg_power'])*100:.1f}%)</li>"
        html += f"<li><b>Rolling & Gravity Resistance:</b> {c['rolling_grav_w']:.1f} W</li>"
        html += "</ul>"

        html += "<h3>Biomechanical Coaching Insights</h3>"
        if raw["pedal_efficiency"] < 65.0:
            html += "<p><b>Low Pedal Efficiency:</b> High radial force wasted at dead centers (0° and 180°). Work on smooth ankle unweighting during the upstroke transition.</p>"
        else:
            html += "<p><b>Optimal Smoothness:</b> Excellent tangential force conversion throughout the pedal stroke.</p>"

        if abs(self.spn_balance.value() - 50.0) > 3.0:
            html += f"<p><b>Left/Right Imbalance:</b> Marked asymmetry detected ({self.spn_balance.value():.1f}% L / {100-self.spn_balance.value():.1f}% R). Unilateral strength training recommended.</p>"

        self.txt_course_summary.setHtml(html)

    def export_csv(self):
        path, _ = QFileDialog.getSaveFileName(self, "Export Cycle Data", "pedal_cycle_kinematics.csv", "CSV Files (*.csv)")
        if path:
            self.cycle_data["df"].to_csv(path, index=False)
            QMessageBox.information(self, "Export Successful", f"Pedal revolution kinematics successfully exported to:\n{path}")

    def export_pdf(self):
        path, _ = QFileDialog.getSaveFileName(self, "Export Performance Report", "cycling_performance_report.pdf", "PDF Files (*.pdf)")
        if path:
            try:
                doc = SimpleDocTemplate(path, pagesize=letter)
                styles = getSampleStyleSheet()
                story = []

                # Title
                title_style = ParagraphStyle('TitleStyle', parent=styles['Heading1'], fontSize=20, leading=24, textColor=colors.HexColor("#2E7D32"))
                story.append(Paragraph("Cycling Biomechanics & Rider Performance Report", title_style))
                story.append(Spacer(1, 15))

                # Rider Parameters Summary
                p_text = f"<b>Rider Mass:</b> {self.spn_mass.value()} kg | <b>Cadence:</b> {self.spn_cadence.value()} RPM | <b>Crank Length:</b> {self.spn_crank.value()} mm"
                story.append(Paragraph(p_text, styles['Normal']))
                story.append(Spacer(1, 15))

                # Cycle Metrics Table
                story.append(Paragraph("Pedal Revolution Kinetic Summary", styles['Heading2']))
                story.append(Spacer(1, 8))

                table_data = [["Kinetic Parameter", "Value"]]
                for k, v in self.cycle_data["metrics"].items():
                    table_data.append([k, v])

                t = Table(table_data, colWidths=[250, 200])
                t.setStyle(TableStyle([
                    ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#2E7D32")),
                    ('TEXTCOLOR', (0,0), (-1,0), colors.whitesmoke),
                    ('ALIGN', (0,0), (-1,-1), 'LEFT'),
                    ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
                    ('BOTTOMPADDING', (0,0), (-1,0), 6),
                    ('GRID', (0,0), (-1,-1), 0.5, colors.grey),
                ]))
                story.append(t)
                story.append(Spacer(1, 20))

                # Performance Simulation Summary
                story.append(Paragraph("Course Simulation Summary", styles['Heading2']))
                story.append(Spacer(1, 8))
                course_text = self.txt_course_summary.toPlainText().replace('\n', '<br/>')
                story.append(Paragraph(course_text, styles['Normal']))

                doc.build(story)
                QMessageBox.information(self, "PDF Export Complete", f"Technical performance report generated successfully:\n{path}")
            except Exception as e:
                QMessageBox.critical(self, "Export Error", f"Failed to generate PDF report:\n{str(e)}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())