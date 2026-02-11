# GesundTech D101 Apex: In-Silico Digital Twin Framework
**A Manufacturer-Centric Platform for Real-Time Health Monitoring and Predictive Maintenance of Infusion Pumps.**

---

## Overview
The **GesundTech D101 Apex** is an *in-silico* Digital Twin framework designed for the medical device industry. Traditional reactive maintenance in hospitals often leads to critical device failure, patient risk, and high recall costs for manufacturers. 

This project addresses these challenges by creating a **Digital Shadow** of a medical infusion pump. Using high-fidelity stochastic modeling, the framework simulates real-time sensor data (Flow, Pressure, Motor Current) to predict mechanical failures—such as tubing occlusions—before they occur.

## Key Features
- **In-Silico Simulation:** High-fidelity virtual modeling of infusion pump sensors (Flow rate, Current, Pressure) with realistic white noise and drift.
- **Predictive Analytics:** Real-time calculation of **Health Scores** and anomaly detection using current-spike analysis.
- **Manufacturer Dashboard:** A professional-grade portal for fleet-wide monitoring, built with **Streamlit**.
- **Fault Injection:** Toggle-based simulation of tubing occlusions to test system response and alerting accuracy.

## 🛠️ Tech Stack
- **Language:** Python 3.9+
- **Simulation/Modeling:** NumPy, Pandas
- **Web Framework:** Streamlit (for the Digital Twin Dashboard)
- **Deployment:** GitHub & Streamlit Cloud

## 📂 Project Structure
```text
├── app.py              # Main Streamlit Dashboard (Manufacturer Portal)
├── simulation.py       # The In-silico Virtual Sensor Engine
├── requirements.txt    # Project dependencies
└── README.md           # Project documentation (this file)
