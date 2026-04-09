import pandas as pd
import matplotlib.pyplot as plt

print("\n--- Food Safety CSV Output ---\n")

# ---------------- LOAD CSV ---------------- #
df = pd.read_csv("inspection_data.csv")

# ---------------- SHOW DATA ---------------- #
print("First 5 Rows:")
print(df.head())

print("\nTotal Rows:", len(df))

# ---------------- FAILED INSPECTIONS ---------------- #
failed = df[df['status'] == 'Fail']
print("\nFailed Inspections:")
print(failed.head())

# ---------------- CONVERT DATE ---------------- #
df['date'] = pd.to_datetime(df['date'])

# =====================================================
# 📊 1. BAR GRAPH (Pass vs Fail)
# =====================================================
status_count = df['status'].value_counts()

plt.figure()
status_count.plot(kind='bar')
plt.title("Inspection Status (Pass vs Fail)")
plt.xlabel("Status")
plt.ylabel("Count")
plt.savefig("status_graph.png")
plt.show()

# =====================================================
# 📈 2. LINE GRAPH (Inspections Over Time)
# =====================================================
date_count = df.groupby('date').size()

plt.figure()
date_count.plot(kind='line')
plt.title("Inspections Over Time")
plt.xlabel("Date")
plt.ylabel("Count")
plt.savefig("time_graph.png")
plt.show()

# =====================================================
# 🥧 3. PIE CHART
# =====================================================
plt.figure()
status_count.plot(kind='pie', autopct='%1.1f%%')
plt.title("Pass vs Fail Percentage")
plt.ylabel("")
plt.savefig("pie_chart.png")
plt.show()

# =====================================================
# 📊 4. HISTOGRAM
# =====================================================
plt.figure()
df['establishment_id'].hist()
plt.title("Inspection Distribution")
plt.xlabel("Establishment ID")
plt.ylabel("Frequency")
plt.savefig("histogram.png")
plt.show()

# =====================================================
# 📊 5. MONTHLY GRAPH
# =====================================================
monthly = df.groupby(df['date'].dt.month).size()

plt.figure()
monthly.plot(kind='bar')
plt.title("Monthly Inspections")
plt.xlabel("Month")
plt.ylabel("Count")
plt.savefig("monthly_graph.png")
plt.show()

# =====================================================
# 📉 6. FAILED TREND GRAPH
# =====================================================
fail_df = df[df['status'] == 'Fail']

plt.figure()
fail_df.groupby('date').size().plot(kind='line')
plt.title("Failed Inspections Over Time")
plt.xlabel("Date")
plt.ylabel("Count")
plt.savefig("fail_trend.png")
plt.show()

# =====================================================
# 👨‍🔧 7. INSPECTOR PERFORMANCE
# =====================================================
inspector = df['inspector_id'].value_counts()

plt.figure()
inspector.plot(kind='bar')
plt.title("Inspector Performance")
plt.xlabel("Inspector ID")
plt.ylabel("Number of Inspections")
plt.savefig("inspector_graph.png")
plt.show()

# ---------------- SAVE OUTPUT CSV ---------------- #
failed.to_csv("failed_inspections.csv", index=False)

print("\n✅ All graphs and output files created successfully!")