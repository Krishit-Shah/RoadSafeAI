# Step-by-step data cleaning and merging for RoadSafeAI
# /ml/road_safe_cleaning.py
# This script cleans and merges accident, casualty, and vehicle datasets for RoadSafeAI.
# It aggregates casualties and vehicles, creates new features, and saves the cleaned dataset.   
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the datasets
accidents = pd.read_csv("../data/AccidentsBig.csv", low_memory=False)
casualties = pd.read_csv("../data/CasualtiesBig.csv", low_memory=False)
vehicles = pd.read_csv("../data/VehiclesBig.csv", low_memory=False)

# --- Step 1: Summarize accidents ---
print("Accidents dataset:")
print(accidents.shape)
print(accidents.columns)

# --- Step 2: Aggregate casualties ---
casualty_summary = casualties.groupby('Accident_Index').agg({
    'Casualty_Severity': 'count'
}).rename(columns={'Casualty_Severity': 'Total_Casualties'}).reset_index()

# --- Step 3: Aggregate vehicles ---
vehicle_summary = vehicles.groupby('Accident_Index').agg({
    'Vehicle_Type': 'nunique'
}).rename(columns={'Vehicle_Type': 'Vehicle_Types_Involved'}).reset_index()

# --- Step 4: Merge datasets ---
acc = accidents.merge(casualty_summary, on='Accident_Index', how='left')
acc = acc.merge(vehicle_summary, on='Accident_Index', how='left')

# Fill missing counts with 0
acc['Total_Casualties'] = acc['Total_Casualties'].fillna(0).astype(int)
acc['Vehicle_Types_Involved'] = acc['Vehicle_Types_Involved'].fillna(0).astype(int)

# --- Step 5: Feature engineering ---
acc['Datetime'] = pd.to_datetime(acc['Date'] + ' ' + acc['Time'], errors='coerce')
acc['Hour'] = acc['Datetime'].dt.hour
acc['Severity_Score'] = acc['Total_Casualties']  # can customize with weights

# --- Step 6: Clean and save ---
keep_columns = [
    'Accident_Index', 'latitude', 'longitude', 'Police_Force', 'Accident_Severity',
    'Number_of_Vehicles', 'Number_of_Casualties', 'Weather_Conditions',
    'Road_Surface_Conditions', 'Light_Conditions', 'Datetime', 'Hour',
    'Total_Casualties', 'Vehicle_Types_Involved', 'Severity_Score'
]
acc_cleaned = acc[keep_columns]

acc_cleaned.to_csv("../data/cleaned_accidents.csv", index=False)
print("✅ Saved cleaned_accidents.csv")
