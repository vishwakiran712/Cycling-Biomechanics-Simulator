# 🚴 Cycling Biomechanics Simulator

> **Sports Technology • Cycling Biomechanics • Performance Engineering • Pedaling Analysis • Power Analysis • Python**

An interactive sports-technology application designed to simulate and analyze key **biomechanical and performance characteristics of cycling**.

The project provides a computational framework for exploring the relationship between **power, cadence, torque, gearing, cycling velocity, resistance, energy expenditure, and pedaling mechanics**.

It is designed as a research and educational platform for:

* Cycling biomechanics
* Athlete performance analysis
* Pedaling technique
* Cycling power analysis
* Performance optimization
* Equipment and gearing analysis
* Sports engineering
* Sports science

<img width="895" height="473" alt="image" src="https://github.com/user-attachments/assets/b25b9caf-628d-4d86-b1f1-118b4f1c96b9" />


---

# 🎯 Project Overview

Cycling performance is determined by the interaction between the athlete, bicycle, environment, and drivetrain.

```text
                    CYCLIST
                       │
          ┌────────────┼────────────┐
          ▼            ▼            ▼
       Cadence        Torque       Position
          │            │            │
          └────────────┼────────────┘
                       ▼
                    POWER
                       │
              ┌────────┴────────┐
              ▼                 ▼
          Drivetrain         Resistance
              │                 │
              └────────┬────────┘
                       ▼
                    VELOCITY
                       │
                       ▼
                 PERFORMANCE
```

The simulator brings these relationships together to demonstrate how changes in cycling parameters influence performance.

---

# 🧠 Cycling Biomechanics

Cycling is a repetitive lower-limb movement involving coordinated motion at the:

* Hip
* Knee
* Ankle

A simplified pedaling chain is:

```text
Hip
 ↓
Thigh
 ↓
Knee
 ↓
Lower Leg
 ↓
Ankle
 ↓
Foot
 ↓
Pedal
 ↓
Crank
```

The cyclist generates muscular force, which is transferred through the crank and drivetrain to produce wheel rotation.

---

# ⚙️ Power, Torque & Cadence

One of the fundamental relationships in cycling is:

```text
Power = Torque × Angular Velocity
```

where:

```text
Angular Velocity = 2π × Cadence / 60
```

Therefore:

```text
P = τ × ω
```

Where:

| Parameter   | Meaning          |
| ----------- | ---------------- |
| **P**       | Power            |
| **τ**       | Crank torque     |
| **ω**       | Angular velocity |
| **Cadence** | Pedaling rate    |

This provides a fundamental basis for analyzing cycling performance.

---

# 🔄 Cadence vs Torque

A cyclist can produce a given power output through different combinations of torque and cadence.

```text
                 POWER
                   │
          ┌────────┴────────┐
          ▼                 ▼
       HIGH TORQUE       HIGH CADENCE
          │                 │
     Lower Cadence      Lower Torque
          │                 │
          └────────┬────────┘
                   ▼
             Same Power
```

This is one of the important performance trade-offs in cycling.

The simulator can be used to explore how changing cadence affects the torque required to maintain a target power output.

---

# 🚴 Pedaling Cycle

A complete crank revolution can be divided into different phases.

```text
              TOP DEAD CENTER
                    0°
                    │
                    ▼
              ┌───────────┐
             /             \
            /               \
     270° ◄                 ► 90°
            \               /
             \             /
              └───────────┘
                    │
                    ▼
             BOTTOM DEAD CENTER
                   180°
```

The pedaling cycle can be considered through:

### 0° — Top Dead Center

Transition between the end of the upstroke and beginning of the downstroke.

### 90° — Power Phase

The crank approaches a mechanically favorable position for force production.

### 180° — Bottom Dead Center

Transition toward the recovery phase.

### 270° — Upstroke

The opposite leg contributes to the next power phase.

---

# 🦵 Joint Biomechanics

Cycling involves coordinated joint motion.

```text
             HIP
              ●
              │
              │
             / 
            ●  KNEE
             \
              \
               ● ANKLE
                \
                 ● PEDAL
```

Potential biomechanical parameters include:

* Hip angle
* Knee angle
* Ankle angle
* Joint range of motion
* Crank position
* Pedal position
* Limb symmetry

These variables can be analyzed to understand pedaling mechanics.

---

# 📐 Joint Angle Analysis

Given three anatomical landmarks:

```text
       A
       ●
      /
     /
    ● B
     \
      \
       ● C
```

The angle at point `B` can be calculated using:

```text
θ = arccos(BA · BC / |BA||BC|)
```

This provides a method for quantifying joint positions throughout the pedal cycle.

For example:

```text
Hip → Knee → Ankle
```

can be used to estimate knee angle.

---

# ⚡ Cycling Power

Mechanical power can be expressed as:

```text
P = τω
```

For a given target power:

```text
Torque = Power / Angular Velocity
```

Therefore:

```text
Higher Cadence
       ↓
Higher Angular Velocity
       ↓
Lower Torque Required

Lower Cadence
       ↓
Lower Angular Velocity
       ↓
Higher Torque Required
```

This relationship is fundamental to understanding cadence selection.

---

# 🛞 Crank & Wheel Mechanics

The crank converts the cyclist's applied force into rotational motion.

```text
        PEDAL FORCE
             ↓
          CRANK
             ↓
       CRANK TORQUE
             ↓
         CHAINRING
             ↓
           CHAIN
             ↓
         CASSETTE
             ↓
         REAR WHEEL
             ↓
          FORWARD
          MOTION
```

The simulator provides a framework for exploring this mechanical transmission.

---

# ⚙️ Gear Ratio

A simplified gear ratio is:

```text
Gear Ratio =
Chainring Teeth
───────────────
Cassette Teeth
```

For example:

```text
50T Chainring
      /
25T Cassette

Gear Ratio = 2.0
```

This means the rear wheel rotates approximately twice for each crank revolution, ignoring other mechanical effects.

---

# 🏁 Cycling Velocity

Wheel speed can be estimated from:

```text
Wheel RPM × Wheel Circumference
```

A simplified relationship is:

```text
Velocity =
Cadence × Gear Ratio × Wheel Circumference
```

after converting the resulting units appropriately.

This allows the simulator to explore:

```text
Cadence
   +
Gear Ratio
   +
Wheel Size
   ↓
Cycling Velocity
```

---

# 🌬️ Cycling Resistance

Cycling performance is affected by several forms of resistance.

```text
                 CYCLIST
                    │
                    ▼
               FORWARD FORCE
                    │
       ┌────────────┼────────────┐
       ▼            ▼            ▼
   Aerodynamic   Rolling       Gradient
      Drag      Resistance     Resistance
       │            │            │
       └────────────┼────────────┘
                    ▼
               TOTAL RESISTANCE
                    │
                    ▼
                 REQUIRED
                  POWER
```

Major resistance components include:

### Aerodynamic Drag

```text
Fᵈ = ½ ρ Cᵈ A v²
```

Aerodynamic drag becomes increasingly important at higher cycling speeds.

### Rolling Resistance

Rolling resistance is influenced by:

* Tire characteristics
* Rider + bicycle mass
* Surface conditions
* Tire pressure

### Gradient Resistance

On an incline, additional power is required to overcome gravity.

```text
P_gravity ≈ m g v sin(θ)
```

---

# ⛰️ Gradient Analysis

The simulator can be extended to investigate cycling on different terrain.

```text
FLAT
────────────────────────────

UPHILL
              /
             /
            /
───────────/

DOWNHILL
───────────\
             \
              \
```

Increasing gradient generally increases the power requirement for a given velocity.

This creates a direct relationship between:

```text
Gradient
   ↓
Required Force
   ↓
Required Power
   ↓
Cycling Performance
```

---

# 📊 Performance Metrics

| Metric           | Purpose                  |
| ---------------- | ------------------------ |
| **Power**        | Mechanical output        |
| **Torque**       | Rotational force         |
| **Cadence**      | Pedaling frequency       |
| **Gear Ratio**   | Drivetrain relationship  |
| **Velocity**     | Cycling speed            |
| **Wheel RPM**    | Wheel rotational speed   |
| **Resistance**   | Opposing forces          |
| **Energy**       | Work performed           |
| **Efficiency**   | Mechanical performance   |
| **Joint Angles** | Biomechanical assessment |

---

# 🧮 Energy & Work

Mechanical work can be expressed as:

```text
Work = Force × Distance
```

For rotational systems:

```text
Work = Torque × Angular Displacement
```

Power is the rate at which work is performed:

```text
Power = Work / Time
```

Therefore:

```text
Work
  ↓
Power
  ↓
Energy Demand
```

This provides a bridge between mechanical cycling performance and physiological demands.

---

# ⚖️ Bilateral Symmetry

Cycling involves repeated contribution from both legs.

```text
             CYCLIST
                │
        ┌───────┴───────┐
        ▼               ▼
      LEFT            RIGHT
       LEG              LEG
        │               │
        ▼               ▼
     Torque          Torque
        │               │
        └───────┬───────┘
                ▼
          TOTAL POWER
```

A future version can compare:

* Left/right torque
* Left/right power
* Joint ROM
* Pedal-force contribution
* Timing differences

This can support identification of bilateral movement differences.

---

# 📈 Torque-Angle Analysis

A more advanced version can model torque throughout the crank cycle.

```text
Torque
  │
  │        ╭──╮
  │       /    \
  │──────╯      ╰────
  │
  └──────────────────── Crank Angle
       0°  90° 180° 270° 360°
```

This enables analysis of:

* Peak torque
* Torque distribution
* Power phase
* Dead spots
* Pedaling smoothness

---

# 🔬 Pedaling Smoothness

An athlete may produce the same average power using different torque profiles.

```text
SMOOTH PEDALING

Torque
  │      ╭────────╮
  │    ╱            ╲
  │───╯              ╰──
  └──────────────────────


LESS SMOOTH PEDALING

Torque
  │        ╭╮
  │       ╱  ╲
  │──────╯    ╰──────
  │
  └──────────────────────
```

Analyzing the torque profile can provide additional information beyond average power.

---

# 🧪 Example Performance Analysis

Consider two cyclists producing the same power:

```text
CYCLIST A

High Cadence
     ↓
Lower Torque
     ↓
Higher Pedaling Frequency


CYCLIST B

Low Cadence
     ↓
Higher Torque
     ↓
Lower Pedaling Frequency
```

Both may produce the same mechanical power while using different biomechanical strategies.

This demonstrates why cycling performance should not be evaluated using a single metric.

---

# 🔄 End-to-End Analysis Pipeline

```text
                  CYCLING INPUT
                       │
                       ▼
              ATHLETE PARAMETERS
                       │
             ┌─────────┼─────────┐
             ▼         ▼         ▼
          Cadence    Torque     Mass
             │         │         │
             └─────────┼─────────┘
                       ▼
                 POWER MODEL
                       │
             ┌─────────┼─────────┐
             ▼         ▼         ▼
          Gearing   Resistance  Gradient
             │         │         │
             └─────────┼─────────┘
                       ▼
                VELOCITY MODEL
                       │
                       ▼
              PERFORMANCE OUTPUT
                       │
             ┌─────────┼─────────┐
             ▼         ▼         ▼
         Metrics    Graphs     Insights
```

---

# 🖥️ Application Concept

The application can be organized as an interactive cycling-performance dashboard:

```text
┌─────────────────────────────────────────────────────────┐
│             CYCLING BIOMECHANICS SIMULATOR              │
├──────────────────────┬──────────────────────────────────┤
│                      │                                  │
│  ATHLETE PARAMETERS  │      PERFORMANCE VISUALIZATION   │
│                      │                                  │
│  Rider Mass          │      Power                       │
│  Cadence             │      Torque                      │
│  Gear Ratio          │      Velocity                    │
│  Gradient             │      Resistance                  │
│                      │                                  │
│  [SIMULATE]          │                                  │
│                      │                                  │
├──────────────────────┴──────────────────────────────────┤
│                    PERFORMANCE METRICS                  │
├───────────────┬───────────────┬─────────────────────────┤
│ Power         │ Torque        │ Cadence                 │
├───────────────┼───────────────┼─────────────────────────┤
│ Velocity      │ Gear Ratio    │ Resistance              │
└───────────────┴───────────────┴─────────────────────────┘
```

---

# 📊 Data Visualization

The simulator can visualize relationships such as:

### Power vs Cadence

```text
Power
  │
  │             ●
  │          ●
  │       ●
  │    ●
  │ ●
  └──────────────────── Cadence
```

### Speed vs Power

```text
Speed
  │
  │             ●
  │          ●
  │       ●
  │    ●
  │ ●
  └──────────────────── Power
```

### Torque vs Cadence

```text
Torque
  │ ●
  │   ●
  │     ●
  │       ●
  │         ●
  └──────────────────── Cadence
```

These plots help demonstrate fundamental cycling-performance relationships.

---

# 🤖 AI & Computer Vision Integration

The simulator can eventually be connected to video-based cycling analysis.

```text
                 CYCLING VIDEO
                       │
                       ▼
                 POSE ESTIMATION
                       │
                       ▼
                BODY LANDMARKS
                       │
                       ▼
               JOINT ANGLE ENGINE
                       │
             ┌─────────┼─────────┐
             ▼         ▼         ▼
           Hip       Knee       Ankle
             │         │         │
             └─────────┼─────────┘
                       ▼
                 PEDAL PHASE
                  DETECTION
                       │
                       ▼
              BIOMECHANICAL DATA
                       │
                       ▼
                 PERFORMANCE
                   ANALYSIS
```

Potential technologies include:

* MediaPipe
* OpenCV
* YOLO Pose
* OpenPose
* Deep-learning pose estimation

---

# 🎥 Video-Based Cycling Analysis

A future version could analyze cycling footage frame-by-frame.

```text
VIDEO
  │
  ▼
FRAME EXTRACTION
  │
  ▼
POSE DETECTION
  │
  ▼
LANDMARK TRACKING
  │
  ▼
JOINT ANGLES
  │
  ▼
CRANK / PEDAL POSITION
  │
  ▼
PEDALING CYCLE
  │
  ▼
BIOMECHANICAL ANALYSIS
```

This could allow automated assessment of cycling technique without dedicated laboratory motion-capture equipment.

---

# 🧬 Advanced Biomechanical Analysis

Future versions could include:

### Joint Kinematics

* Hip flexion/extension
* Knee flexion/extension
* Ankle dorsiflexion/plantarflexion

### Pedaling Mechanics

* Crank angle
* Torque profile
* Power phase
* Cadence
* Pedal smoothness

### Symmetry

* Left/right joint motion
* Left/right power
* Left/right torque
* Timing differences

### Position Analysis

* Saddle height
* Handlebar position
* Trunk angle
* Knee-over-pedal relationship

---

# 🚴 Bike-Fit Analysis

A future extension can connect biomechanics with bicycle fitting.

```text
                 CYCLIST
                    │
          ┌─────────┼─────────┐
          ▼         ▼         ▼
        Saddle    Handlebar  Crank
        Height     Position   Length
          │         │         │
          └─────────┼─────────┘
                    ▼
             BODY POSITION
                    │
                    ▼
             JOINT ANGLES
                    │
                    ▼
             PEDAL MECHANICS
                    │
                    ▼
              PERFORMANCE
```

Potential applications:

* Saddle-height optimization
* Cleat-position analysis
* Handlebar position
* Reach analysis
* Knee-angle optimization
* Aerodynamic position assessment

---

# 🌬️ Aerodynamic Performance

At higher speeds, aerodynamic drag becomes increasingly important.

```text
                    AIRFLOW
                       ↓
                 ┌─────────┐
                 │ CYCLIST │
                 └─────────┘
                       ↓
                 AIR RESISTANCE
                       ↓
                 REQUIRED POWER
```

A future version could compare different riding positions:

```text
Upright
   ↓
Higher Frontal Area
   ↓
Higher Drag


Aero Position
   ↓
Lower Frontal Area
   ↓
Lower Drag
```

This provides a bridge between **biomechanics and cycling engineering**.

---

# 🧠 Cycling Performance Digital Twin

The long-term vision is to evolve the simulator into a **Cycling Performance Digital Twin**.

```text
                 REAL CYCLIST
                      │
          ┌───────────┼───────────┐
          ▼           ▼           ▼
        Video      Wearables    Bike Sensors
          │           │           │
          └───────────┼───────────┘
                      ▼
                 DIGITAL TWIN
                      │
          ┌───────────┼───────────┐
          ▼           ▼           ▼
      Biomechanics  Physiology  Equipment
          │           │           │
          └───────────┼───────────┘
                      ▼
                 SIMULATION
                      │
          ┌───────────┼───────────┐
          ▼           ▼           ▼
       Technique    Power       Strategy
      Optimization Prediction   Modeling
```

The objective would be to create a computational representation of the cyclist that can be used to explore performance scenarios.

---

# 🏆 Potential Applications

| Application              | Example                          |
| ------------------------ | -------------------------------- |
| **Performance Analysis** | Power and cadence optimization   |
| **Biomechanics**         | Joint-motion analysis            |
| **Bike Fitting**         | Position optimization            |
| **Training**             | Cadence and power strategy       |
| **Equipment Analysis**   | Gearing and wheel effects        |
| **Aerodynamics**         | Riding-position analysis         |
| **Coaching**             | Technique feedback               |
| **Research**             | Cycling biomechanics experiments |

---

# 🛠️ Technology Stack

| Technology     | Purpose                       |
| -------------- | ----------------------------- |
| **Python**     | Core application              |
| **NumPy**      | Numerical calculations        |
| **Pandas**     | Data processing               |
| **Matplotlib** | Data visualization            |
| **PyQt5**      | Interactive desktop interface |

The application is built around Python's scientific-computing ecosystem.

---

# 📂 Project Structure

```text
Cycling-Biomechanics-Simulator/
│
├── app.py
├── README.md
└── LICENSE
```

The primary application logic is contained in:

```text
app.py
```

Conceptually:

```text
app.py
 │
 ├── Input Parameters
 │
 ├── Cycling Mechanics
 │
 ├── Power / Torque Model
 │
 ├── Resistance Model
 │
 ├── Performance Simulation
 │
 ├── Visualization
 │
 └── User Interface
```

---

# 🚀 Getting Started

## 1. Clone the repository

```bash
git clone https://github.com/vishwakiran712/Cycling-Biomechanics-Simulator.git

cd Cycling-Biomechanics-Simulator
```

## 2. Install dependencies

```bash
pip install numpy pandas matplotlib PyQt5
```

## 3. Run the application

```bash
python app.py
```

The **Cycling Biomechanics Simulator** will launch.

---

# 🧪 Example Workflow

### Step 1 — Configure the Cyclist

Enter parameters such as:

* Rider mass
* Cadence
* Power
* Gear ratio
* Gradient

### Step 2 — Simulate

Run the cycling-performance model.

### Step 3 — Analyze

Evaluate:

```text
Power
Torque
Cadence
Velocity
Resistance
```

### Step 4 — Visualize

Examine relationships between cycling variables.

### Step 5 — Optimize

Explore how changes in:

```text
Cadence
Gearing
Power
Gradient
```

affect performance.

---

# 🔮 Development Roadmap

## Phase 1 — Cycling Mechanics

* [x] Power modeling
* [x] Torque analysis
* [x] Cadence analysis
* [x] Gear-ratio modeling
* [x] Velocity simulation
* [x] Resistance concepts

## Phase 2 — Biomechanics

* [ ] Joint-angle analysis
* [ ] Crank-cycle analysis
* [ ] Pedaling symmetry
* [ ] Torque-angle modeling
* [ ] Pedaling smoothness

## Phase 3 — Computer Vision

* [ ] Video input
* [ ] Pose estimation
* [ ] Pedal tracking
* [ ] Joint tracking
* [ ] Automatic crank-angle estimation

## Phase 4 — Advanced Performance

* [ ] Aerodynamic modeling
* [ ] Gradient simulation
* [ ] Bike-fit analysis
* [ ] Equipment optimization
* [ ] Energy expenditure modeling

## Phase 5 — AI & Digital Twin

* [ ] Technique classification
* [ ] Performance prediction
* [ ] Personalized optimization
* [ ] AI coaching recommendations
* [ ] Cycling performance digital twin

---

# 🏗️ Future Platform Architecture

```text
                         CYCLIST
                            │
                            ▼
                    CYCLING VIDEO
                            │
                            ▼
                    POSE ESTIMATION
                            │
                            ▼
                  SKELETAL LANDMARKS
                            │
          ┌─────────────────┼─────────────────┐
          ▼                 ▼                 ▼
       Hip Angle         Knee Angle       Ankle Angle
          │                 │                 │
          └─────────────────┼─────────────────┘
                            ▼
                     PEDAL ANALYSIS
                            │
          ┌─────────────────┼─────────────────┐
          ▼                 ▼                 ▼
       Cadence            Torque            Power
          │                 │                 │
          └─────────────────┼─────────────────┘
                            ▼
                  CYCLING DYNAMICS ENGINE
                            │
          ┌─────────────────┼─────────────────┐
          ▼                 ▼                 ▼
       Resistance        Gearing         Gradient
          │                 │                 │
          └─────────────────┼─────────────────┘
                            ▼
                    PERFORMANCE ENGINE
                            │
          ┌─────────────────┼─────────────────┐
          ▼                 ▼                 ▼
      Technique          Prediction       Optimization
                            │
                            ▼
                    ATHLETE DASHBOARD
```

---

# ⚠️ Important Limitations

Cycling performance is influenced by numerous factors, including:

* Rider physiology
* Body morphology
* Bicycle geometry
* Cadence
* Torque
* Gear selection
* Aerodynamics
* Tire characteristics
* Road surface
* Gradient
* Wind
* Fatigue
* Measurement accuracy

The equations used in a simplified simulator cannot fully represent the complexity of real-world cycling biomechanics, physiology, and fluid dynamics.

This project is intended for **research, education and prototyping**, not as a substitute for laboratory-grade cycling analysis or professional bike-fitting assessment.

---

# 📌 Project Status

**Status:** 🟢 Sports Technology Prototype

### Core objectives

* ✅ Cycling performance simulation
* ✅ Biomechanical framework
* ✅ Power and torque analysis
* ✅ Cadence analysis
* ✅ Gear-ratio modeling
* ✅ Resistance concepts
* ✅ Performance visualization
* 🔄 Advanced pedaling biomechanics
* 🔄 Computer-vision integration
* 🔄 AI-powered performance optimization
* 🔄 Cycling digital twin

---

# 👨‍💻 Author

**Vishwakiran B.V.S.**

Sports Technology • Biomechanics • AI & Computer Vision • Athlete Analytics • Product Research

GitHub:
https://github.com/vishwakiran712

---

# 📄 License

This project is licensed under the **MIT License**.

See the [LICENSE](LICENSE) file for details.

---

## ⭐ Project Philosophy

> **Measure the pedal stroke. Model the mechanics. Optimize the rider.**
