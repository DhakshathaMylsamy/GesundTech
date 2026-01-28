import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="GesundTech Manufacturer Portal", layout="wide")

# Branding
st.sidebar.title("GesundTech")
st.sidebar.image("https://via.placeholder.com/150?text=GesundTech+Logo") # Replace with your logo
st.sidebar.info("Model: D101 Apex Series")

# Main Header
st.title("Digital Twin Fleet Dashboard")

# Top Level Metrics
m1, m2, m3, m4 = st.columns(4)
m1.metric("Active Units", "1,240", "Online")
m2.metric("Critical Alerts", "3", "-1", delta_color="inverse")
m3.metric("Avg. Motor Health", "94%", "Stable")
m4.metric("Pending Updates", "12", "D101-v2.1")

# Digital Twin Simulation
st.divider()
col_left, col_right = st.columns([1, 2])

with col_left:
    st.subheader("Asset Twin: D101-SN882")
    # You can embed a 3D model here later using pythreejs
    st.image("https://via.placeholder.com/300x400?text=3D+Pump+Model", caption="Live Twin State")
    if st.button("Run Diagnostic"):
        st.write("Diagnostic complete: All systems nominal.")

with col_right:
    st.subheader("Real-Time Telemetry (Simulated)")
    # Simulating pump data
    chart_data = pd.DataFrame(np.random.randn(20, 2), columns=['Flow Rate (mL/h)', 'Motor Current (mA)'])
    st.line_chart(chart_data)

# Predictive Maintenance Table
st.subheader("Predictive Maintenance Schedule")
data = {
    "Pump ID": ["D101-102", "D101-405", "D101-009"],
    "Hospital": ["City Med", "Apollo", "General Hosp"],
    "Predicted Issue": ["Motor Strain", "Battery Degradation", "Flow Anomaly"],
    "Confidence": ["92%", "88%", "75%"]
}
st.table(data)