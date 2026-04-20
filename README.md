# 🏥 CareMetrics Project

## 📊 Hospital Operations and Patient Flow Analytics

CareMetrics is a healthcare analytics project designed to analyze hospital patient flow using SQL and Python.
It identifies bottlenecks, delays, and workload patterns to improve operational efficiency and patient experience.

---

## 🚀 Features

* Patient flow analysis across hospital stages
* Delay detection (registration → consultation → diagnostics → billing)
* Peak hour identification
* Capacity and workload analysis
* Data visualization dashboards

---

## 🛠️ Tech Stack

* **Python** (Pandas, Matplotlib)
* **MySQL**
* **CSV Dataset (`events.csv`)**

---

## 📁 Project Structure

```
CareMetrics_Project/
│
├── data/              # Dataset (events.csv)
├── sql/               # SQL queries
├── src/               # Python scripts
├── dashboards/        # Generated graphs
├── reports/           # Insights report
└── README.md
```

---

## ⚙️ How to Run

1. Clone the repository
2. Install dependencies:

   ```
   pip install pandas matplotlib sqlalchemy mysql-connector-python
   ```
3. Ensure MySQL is running and update connection in code:

   ```
   create_engine("mysql+mysqlconnector://user:password@localhost/db")
   ```
4. Run analysis:

   ```
   python src/capacity_analysis.py
   ```

---

## 📊 Key KPIs

* Average Waiting Time
* Consultation → Diagnostics Delay
* Diagnostics → Billing Delay
* Total Hospital Time (Length of Stay)
* Peak Hour Load

---

## 📊 Dashboards

### Event Distribution

![Event Distribution](dashboards/bed_utilization.png)

### Hourly Patient Flow

![Hourly Flow](dashboards/staff_demand.png)

### Delays Analysis

![Delays](dashboards/delays.png)

### Peak Hour Detection

![Peak Hour](dashboards/peak_hour.png)

### Waiting Time Analysis

![Waiting Time](dashboards/wait_time.png)

---

## 📌 Key Insights

* Peak activity occurs between **9 AM – 12 PM**
* Diagnostics stage is the **primary bottleneck**
* Patient load is **unevenly distributed across time**
* Peak hours require **additional staffing and resource allocation**

---

## 🎯 Outcome

This project helps hospital administrators to:

* Reduce patient waiting time
* Improve workflow efficiency
* Optimize staffing and resource allocation
* Identify operational bottlenecks

---

## 📄 Insights Report

Detailed findings available in:

```
reports/insights.txt
```

---

## 💡 Future Improvements

* Real-time dashboard integration
* Machine learning for congestion prediction
* Web-based analytics interface
