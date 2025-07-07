import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("../data/cleaned_accidents.csv")

print(df.describe())

# Correlation Heatmap
numeric_cols = df.select_dtypes(include='number')
sns.heatmap(numeric_cols.corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()

# Boxplot for Severity Score
sns.boxplot(x=df['Severity_Score'])
plt.title("Severity Score Boxplot")
plt.show()

# Accidents by Hour
df['Hour'].value_counts().sort_index().plot(kind='bar')
plt.title("Accidents by Hour")
plt.xlabel("Hour")
plt.ylabel("Count")
plt.show()

plt.savefig("D:\RoadSafeAI\RoadSafeAI/docs\eda_charts/heatmap.png")
plt.savefig("D:\RoadSafeAI\RoadSafeAI\docs\eda_charts/severity_boxplot.png")
plt.savefig("D:\RoadSafeAI\RoadSafeAI\docs\eda_charts/hourly_bar.png")

