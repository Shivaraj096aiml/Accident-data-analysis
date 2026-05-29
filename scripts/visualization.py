import os

# Create folder
os.makedirs("outputs/graphs", exist_ok=True)



import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
accidents = pd.read_csv(r"C:\Users\shiva\OneDrive\Desktop\accident_analysis_project\data\Dataset_after_cleaning\clean_accidents.csv")
vehicles = pd.read_csv(r"C:\Users\shiva\OneDrive\Desktop\accident_analysis_project\data\Dataset_after_cleaning\clean_vehicles.csv")
casualties = pd.read_csv(r"C:\Users\shiva\OneDrive\Desktop\accident_analysis_project\data\Dataset_after_cleaning\clean_casualties.csv")
roads = pd.read_csv(r"C:\Users\shiva\OneDrive\Desktop\accident_analysis_project\data\Dataset_after_cleaning\clean_road_conditions.csv")

# Merge
df = accidents.merge(vehicles, on='accident_id') \
              .merge(casualties, on='accident_id') \
              .merge(roads, on='accident_id')

# 1. Location
df['location'].value_counts().plot(kind='bar')
plt.title("Accidents by Location")
plt.savefig("outputs/graphs/location.png")
plt.clf()

# 2. Time of Day
sns.countplot(x='time_of_day', data=df)
plt.title("Accidents by Time")
plt.savefig("outputs/graphs/time.png")
plt.clf()

# 3. Vehicle Type
sns.countplot(x='vehicle_type', data=df)
plt.xticks(rotation=45)
plt.title("Vehicle Type Impact")
plt.savefig("outputs/graphs/vehicle.png")
plt.clf()

# 4. Severity
sns.countplot(x='severity', data=df)
plt.title("Severity Distribution")
plt.savefig("outputs/graphs/severity.png")
plt.clf()

# 5. Weather vs Severity
sns.countplot(x='weather', hue='severity', data=df)
plt.xticks(rotation=45)
plt.title("Weather Impact")
plt.savefig("outputs/graphs/weather.png")
plt.clf()

# 6. Driver Behavior
sns.countplot(x='driver_behavior', data=df)
plt.xticks(rotation=45)
plt.title("Driver Behavior")
plt.savefig("outputs/graphs/behavior.png")
plt.clf()

print("✅ All graphs saved in outputs/graphs/")