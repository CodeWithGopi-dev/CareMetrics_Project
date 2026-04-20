import pandas as pd
import matplotlib.pyplot as plt
import os

# ===============================
# SETUP
# ===============================
os.makedirs("dashboards", exist_ok=True)

# ===============================
# LOAD DATA
# ===============================
df = pd.read_csv("data/events.csv")
print("Columns:", df.columns)

# ===============================
# CLEAN DATA
# ===============================
df['event_type'] = df['event_type'].str.lower().str.strip()
df['timestamp'] = pd.to_datetime(df['timestamp'])

# ===============================
# 1. EVENT DISTRIBUTION
# ===============================
bed_usage = df['event_type'].value_counts()

plt.figure(figsize=(8,5))
bed_usage.plot(kind='bar')
plt.title("Event Distribution (Hospital Flow)")
plt.xlabel("Event Type")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.tight_layout()
plt.savefig("dashboards/bed_utilization.png")

# ===============================
# 2. STAFF DEMAND (HOURLY)
# ===============================
df['hour'] = df['timestamp'].dt.hour
hourly = df['hour'].value_counts().sort_index()

plt.figure(figsize=(8,5))
hourly.plot(kind='line', marker='o')
plt.title("Patient Flow by Hour")
plt.xlabel("Hour")
plt.ylabel("Number of Events")
plt.grid(True)
plt.tight_layout()
plt.savefig("dashboards/staff_demand.png")

# ===============================
# SORT DATA (IMPORTANT)
# ===============================
df = df.sort_values(['patient_id', 'timestamp'])

# ===============================
# 3. WAIT TIME (Registration → Consultation)
# ===============================
reg = df[df['event_type'] == 'registration']
consult = df[df['event_type'] == 'consultation']

wait = pd.merge(reg, consult, on='patient_id')
wait = wait[wait['timestamp_y'] > wait['timestamp_x']]

wait['wait_time'] = (
    wait['timestamp_y'] - wait['timestamp_x']
).dt.total_seconds() / 60

plt.figure()
plt.bar(wait['patient_id'], wait['wait_time'])
plt.title("Wait Time per Patient")
plt.xlabel("Patient ID")
plt.ylabel("Minutes")
plt.tight_layout()
plt.savefig("dashboards/wait_time.png")

# ===============================
# 4. DELAYS
# ===============================
diag = df[df['event_type'] == 'diagnostics']
bill = df[df['event_type'] == 'billing']

cd = pd.merge(consult, diag, on='patient_id')
cd = cd[cd['timestamp_y'] > cd['timestamp_x']]
cd['delay'] = (
    cd['timestamp_y'] - cd['timestamp_x']
).dt.total_seconds() / 60

db = pd.merge(diag, bill, on='patient_id')
db = db[db['timestamp_y'] > db['timestamp_x']]
db['delay'] = (
    db['timestamp_y'] - db['timestamp_x']
).dt.total_seconds() / 60

delay_names = ["Consult→Diagnosis", "Diagnosis→Billing"]
delay_values = [cd['delay'].mean(), db['delay'].mean()]

plt.figure()
plt.bar(delay_names, delay_values)
plt.title("Delays in Patient Flow")
plt.ylabel("Minutes")
plt.tight_layout()
plt.savefig("dashboards/delays.png")

# ===============================
# 5. PEAK HOURS
# ===============================
peak = df.groupby('hour').size()

plt.figure()
peak.plot(kind='bar')
plt.title("Peak Hour Analysis")
plt.xlabel("Hour")
plt.ylabel("Patients")
plt.tight_layout()
plt.savefig("dashboards/peak_hour.png")

# ===============================
# DONE
# ===============================
print("All analysis completed ✅")