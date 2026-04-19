import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine
import os

# ===============================
# CREATE DASHBOARD FOLDER
# ===============================
os.makedirs("dashboards", exist_ok=True)

# ===============================
# CONNECT TO MYSQL
# ===============================
engine = create_engine("mysql+mysqlconnector://gopi:1234@localhost/caremetrics")


df = pd.read_sql("SELECT * FROM events", engine)

# Save to Excel
df.to_excel("data/sql_events.xlsx", index=False)

print("SQL data exported to Excel!")

# ===============================
# LOAD DATA
# ===============================
query = "SELECT * FROM events"
df = pd.read_sql(query, engine)

# Convert timestamp
df['timestamp'] = pd.to_datetime(df['timestamp'])

# ===============================
# WAIT TIME (Registration → Consultation)
# ===============================
reg = df[df['event_type'] == 'registration']
consult = df[df['event_type'] == 'consultation']

wait = pd.merge(reg, consult, on='patient_id')
wait['wait_time'] = (wait['timestamp_y'] - wait['timestamp_x']).dt.total_seconds() / 60

print("Average Wait Time (minutes):", round(wait['wait_time'].mean(), 2))

# ===============================
# CONSULT → DIAGNOSIS
# ===============================
consult = df[df['event_type'] == 'consultation']
diag = df[df['event_type'] == 'diagnostics']

cd = pd.merge(consult, diag, on='patient_id')
cd['delay'] = (cd['timestamp_y'] - cd['timestamp_x']).dt.total_seconds() / 60

print("Consult → Diagnosis Delay (minutes):", round(cd['delay'].mean(), 2))

# ===============================
# DIAGNOSIS → BILLING
# ===============================
diag = df[df['event_type'] == 'diagnostics']
bill = df[df['event_type'] == 'billing']

db = pd.merge(diag, bill, on='patient_id')
db['delay'] = (db['timestamp_y'] - db['timestamp_x']).dt.total_seconds() / 60

print("Diagnosis → Billing Delay (minutes):", round(db['delay'].mean(), 2))

# ===============================
# TOTAL HOSPITAL TIME
# ===============================
reg = df[df['event_type'] == 'registration']
dis = df[df['event_type'] == 'discharge']

td = pd.merge(reg, dis, on='patient_id')
td['total_time'] = (td['timestamp_y'] - td['timestamp_x']).dt.total_seconds() / 3600

print("Total Hospital Time (hours):", round(td['total_time'].mean(), 2))

# ===============================
# PEAK HOURS GRAPH
# ===============================
df['hour'] = df['timestamp'].dt.hour
peak = df.groupby('hour').size()

plt.figure()
peak.plot(kind='bar')
plt.title("Peak Hour Analysis")
plt.xlabel("Hour")
plt.ylabel("Patient Count")
plt.savefig("dashboards/peak_hour.png")
plt.show()

# ===============================
# WAIT TIME GRAPH
# ===============================
plt.figure()
plt.bar(wait['patient_id'], wait['wait_time'])
plt.title("Wait Time per Patient")
plt.xlabel("Patient ID")
plt.ylabel("Wait Time (minutes)")
plt.savefig("dashboards/wait_time.png")
plt.show()

# ===============================
# DELAYS GRAPH
# ===============================
delay_names = ["Consult→Diagnosis", "Diagnosis→Billing"]
delay_values = [
    cd['delay'].mean(),
    db['delay'].mean()
]

plt.figure()
plt.bar(delay_names, delay_values)
plt.title("Delays in Patient Flow")
plt.xlabel("Stages")
plt.ylabel("Time (minutes)")
plt.savefig("dashboards/delays.png")
plt.show()