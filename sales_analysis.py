

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# Project folders
BASE_DIR = Path(__file__).resolve().parent.parent
OUTPUT_DIR = BASE_DIR / "python"
OUTPUT_DIR.mkdir(exist_ok=True)

# Load Excel data
file_path = r"C:\Users\Akash\Downloads\excel_sales_dashboard (1) copy.xlsx"
df = pd.read_excel(file_path, sheet_name="Clean_Data")

# Data cleaning
df.columns = df.columns.str.strip()
df = df.drop_duplicates()
df["Order_Date"] = pd.to_datetime(df["Order_Date"], errors="coerce")
df["Quantity"] = pd.to_numeric(df["Quantity"], errors="coerce")
df["Unit_Price"] = pd.to_numeric(df["Unit_Price"], errors="coerce")
df["Revenue"] = pd.to_numeric(df["Revenue"], errors="coerce")

df = df.dropna(subset=[
    "Order_ID", "Order_Date", "Product", "Quantity", "Unit_Price", "Revenue"
])

# Save cleaned dataset
df.to_csv(OUTPUT_DIR / "cleaned_sales_data.csv", index=False)

# Calculate KPIs
total_revenue = df["Revenue"].sum()
total_orders = df["Order_ID"].nunique()
units_sold = df["Quantity"].sum()
avg_order_value = total_revenue / total_orders if total_orders else 0

kpis = pd.DataFrame({
    "Metric": ["Total Revenue (INR)", "Distinct Orders",
               "Units Sold", "Average Order Value (INR)"],
    "Value": [total_revenue, total_orders, units_sold, avg_order_value]
})
kpis.to_csv(OUTPUT_DIR / "sales_kpis.csv", index=False)

# Product revenue chart
product_revenue = df.groupby("Product")["Revenue"].sum().sort_values()

plt.figure(figsize=(10, 6))
product_revenue.plot(kind="barh")
plt.title("Revenue by Product")
plt.xlabel("Revenue (INR)")
plt.ylabel("Product")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "revenue_by_product.png")
plt.close()

# Monthly revenue chart
monthly_revenue = df.groupby("Month")["Revenue"].sum().sort_index()

plt.figure(figsize=(10, 5))
monthly_revenue.plot(kind="line", marker="o")
plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue (INR)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "monthly_revenue_trend.png")
plt.close()

# EDA report
missing_values = int(df.isna().sum().sum())
duplicates = int(df.duplicated().sum())
top_product = df.groupby("Product")["Revenue"].sum().idxmax()
top_product_revenue = df.groupby("Product")["Revenue"].sum().max()
top_region = df.groupby("Region")["Revenue"].sum().idxmax()
top_region_revenue = df.groupby("Region")["Revenue"].sum().max()

report = f"""
WEEK 1 SALES DATA ANALYSIS — EDA REPORT

Dataset rows after cleaning: {len(df)}
Number of columns: {len(df.columns)}
Missing values remaining: {missing_values}
Duplicate rows remaining: {duplicates}

BUSINESS KPIs
Total revenue: INR {total_revenue:,.2f}
Distinct orders: {total_orders}
Units sold: {units_sold:,.0f}
Average order value: INR {avg_order_value:,.2f}

KEY INSIGHTS
Top product by revenue: {top_product} (INR {top_product_revenue:,.2f})
Top region by revenue: {top_region} (INR {top_region_revenue:,.2f})

Revenue is summarized by product and month in the generated charts.
This is a synthetic practice dataset; findings are for learning purposes.
"""

(OUTPUT_DIR / "EDA_Report.txt").write_text(report, encoding="utf-8")

print("Analysis completed successfully!")
print(kpis.to_string(index=False))
print("\nTop product:", top_product)
print("Top region:", top_region)
print("\nFiles saved in:", OUTPUT_DIR)
