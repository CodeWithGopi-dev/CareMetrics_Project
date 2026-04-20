import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_excel("data/events.xlsx")

print("Columns:", df.columns)

# -------------------------------
# 1. Bed utilization (using event_type)
# -------------------------------
bed_usage = df['event_type'].value_counts()

plt.figure()
bed_usage.plot(kind='bar')
plt.title("Event Distribution (Hospital Flow)")
plt.xlabel("Event Type")
plt.ylabel("Count")
plt.savefig("dashboards/bed_utilization.png")

# -------------------------------
# 2. Staff demand (hourly load)
# -------------------------------
df['hour'] = pd.to_datetime(df['timestamp']).dt.hour

hourly = df['hour'].value_counts().sort_index()

plt.figure()
hourly.plot(kind='line', marker='o')
plt.title("Patient Flow by Hour")
plt.xlabel("Hour")
plt.ylabel("Number of Events")
plt.savefig("dashboards/staff_demand.png")

print("Capacity analysis completed!")