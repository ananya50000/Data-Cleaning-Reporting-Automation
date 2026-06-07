import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv("superstore.csv", encoding="latin1")

print("Dataset Loaded Successfully")

# Remove Duplicates
df = df.drop_duplicates()

# Fill Missing Values
df = df.fillna(0)

# Save Cleaned Data
df.to_csv("cleaned_data.csv", index=False)

print("Cleaned Data Saved")

# Automated Report
report = pd.DataFrame({
    "Metric": [
        "Total Records",
        "Total Sales",
        "Total Profit",
        "Average Sales"
    ],
    "Value": [
        len(df),
        df["Sales"].sum(),
        df["Profit"].sum(),
        df["Sales"].mean()
    ]
})

report.to_csv(
    "automation_report.csv",
    index=False
)

print("Report Generated")

# Visualization
sales = df.groupby("Category")["Sales"].sum()

plt.figure(figsize=(8,5))

sales.plot(kind="bar")

plt.title("Automated Sales Report")

plt.xlabel("Category")

plt.ylabel("Sales")

plt.tight_layout()

plt.savefig("automation_chart.png")

plt.show()

print("Project Completed Successfully")