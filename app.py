import streamlit as st
import pandas as pd
import numpy as np
import time
from datetime import datetime

# --- CONFIGURATION ---
st.set_page_config(page_title="GesundTech Manufacturer Portal", layout="wide")

st.title("GesundTech D101 Apex: Digital Twin Portal")
st.markdown("### Real-Time Fleet Analytics & Predictive Maintenance")

# --- SIDEBAR CONTROL ---
st.sidebar.header("Asset Controls")
device_id = st.sidebar.selectbox("Select Device", ["D101-SN882", "D101-SN904"])
simulate_issue = st.sidebar.toggle("Simulate Tubing Occlusion")

# --- DATA GENERATION ENGINE ---
def get_telemetry():
    """Generates a row of data based on the toggle state."""
    if not simulate_issue:
        curr, pres, flow = 150 + np.random.normal(0, 2), 5 + np.random.normal(0, 0.1), 20.0
        status = "✅ Healthy"
        health_score = 98
    else:
        curr, pres, flow = 420 + np.random.normal(0, 5), 22 + np.random.normal(0, 1), 4.2
        status = "⚠️ WARNING: Occlusion"
        health_score = 35
    
    return curr, pres, flow, status, health_score

# --- DASHBOARD LAYOUT ---
col1, col2, col3, col4 = st.columns(4)

# Placeholder for real-time updates
curr_val, pres_val, flow_val, status_val, health_val = get_telemetry()

col1.metric("Motor Current", f"{curr_val:.1f} mA")
col2.metric("Line Pressure", f"{pres_val:.1f} psi")
col3.metric("Flow Rate", f"{flow_val:.1f} mL/h")
col4.metric("Asset Health", f"{health_val}%")

st.divider()

# --- LIVE CHARTING ---
st.subheader("Live Asset Telemetry")
if 'history' not in st.session_state:
    st.session_state.history = pd.DataFrame(columns=['Time', 'Current', 'Pressure'])

# Create a loop to update the dashboard
new_data = pd.DataFrame({
    'Time': [datetime.now().strftime("%H:%M:%S")],
    'Current': [curr_val],
    'Pressure': [pres_val]
})

st.session_state.history = pd.concat([st.session_state.history, new_data]).tail(20)
st.line_chart(st.session_state.history.set_index('Time'))

if simulate_issue:
    st.error(f"**Action Required:** High pressure detected in {device_id}. Predictive model suggests mechanical strain.")
else:
    st.success(f"**System Nominal:** {device_id} is operating within safety parameters.")

# Auto-refresh the page
time.sleep(2)
st.rerun()
