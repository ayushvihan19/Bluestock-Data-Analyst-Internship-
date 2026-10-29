
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Change this path to the actual location of your Excel file
file_path = r"C:\Users\Akash\Downloads\excel_sales_dashboard (1) copy.xlsx"

df = pd.read_excel(file_path, sheet_name="Clean_Data")

print("First 5 rows:")
print(df.head())

print("\nDataset shape:")
print(df.shape)

print("\nColumn names:")
print(df.columns.tolist())

print("\nMissing values:")
print(df.isnull().sum())

print("\nDuplicate rows:", df.duplicated().sum())
