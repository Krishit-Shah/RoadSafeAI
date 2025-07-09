import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load data
df = pd.read_csv("../data/cleaned_accidents.csv")

# Create output folder if it doesn't exist
output_folder = "../docs/eda_charts"
os.makedirs(output_folder, exist_ok=True)

print(df.describe())

# --- 1. Correlation Heatmap ---
plt.figure(figsize=(10, 6))
numeric_cols = df.select_dtypes(include='number')
sns.heatmap(numeric_cols.corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig(f"{output_folder}/heatmap.png")
plt.show()

# --- 2. Boxplot for Severity Score ---
plt.figure(figsize=(8, 4))
sns.boxplot(x=df['Severity_Score'])
plt.title("Severity Score Boxplot")
plt.tight_layout()
plt.savefig(f"{output_folder}/severity_boxplot.png")
plt.show()

# --- 3. Bar plot: Accidents by Hour ---
plt.figure(figsize=(10, 4))
df['Hour'].value_counts().sort_index().plot(kind='bar', color='skyblue')
plt.title("Accidents by Hour")
plt.xlabel("Hour")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig(f"{output_folder}/hourly_bar.png")
plt.show()
