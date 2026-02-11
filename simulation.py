import time
import random
import pandas as pd
from datetime import datetime

class GesundTechD101:
    def __init__(self, device_id):
        self.device_id = device_id
        self.base_current = 150.0  # Normal motor current in mA
        self.base_pressure = 5.0    # Normal tubing pressure in psi
        self.flow_rate = 20.0       # Set flow rate in mL/h
        self.status = "Healthy"
        
    def generate_telemetry(self, simulate_failure=False):
        """Generates one row of 'In-Silico' sensor data."""
        
        # Add 'White Noise' to make data look real
        noise_current = random.uniform(-2, 2)
        noise_pressure = random.uniform(-0.1, 0.1)
        
        if not simulate_failure:
            current = self.base_current + noise_current
            pressure = self.base_pressure + noise_pressure
            self.status = "Healthy"
        else:
            # SIMULATE OCCLUSION: Current and Pressure rise, Flow drops
            current = self.base_current + random.uniform(200, 300) 
            pressure = self.base_pressure + random.uniform(15, 25)
            self.flow_rate = max(0, self.flow_rate - random.uniform(5, 10))
            self.status = "Warning: Occlusion Detected"

        return {
            "Timestamp": datetime.now().strftime("%H:%M:%S"),
            "Device_ID": self.device_id,
            "Flow_Rate_mLh": round(self.flow_rate, 2),
            "Motor_Current_mA": round(current, 2),
            "Pressure_psi": round(pressure, 2),
            "Status": self.status
        }

# --- TEST THE SIMULATION ---
pump = GesundTechD101("D101-SN882")

print(f"Starting In-Silico stream for {pump.device_id}...")
print("-" * 60)

for i in range(10):
    # After 5 readings, let's simulate a failure
    fail = True if i >= 6 else False
    data = pump.generate_telemetry(simulate_failure=fail)
    print(data)
    time.sleep(1) # Wait 1 second between 'sensor' reads
