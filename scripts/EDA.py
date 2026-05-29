import pandas as pd

# Load cleaned data
accidents = pd.read_csv(r"C:\Users\shiva\OneDrive\Desktop\accident_analysis_project\data\Dataset_after_cleaning\clean_accidents.csv")
vehicles = pd.read_csv(r"C:\Users\shiva\OneDrive\Desktop\accident_analysis_project\data\Dataset_after_cleaning\clean_vehicles.csv")
casualties = pd.read_csv(r"C:\Users\shiva\OneDrive\Desktop\accident_analysis_project\data\Dataset_after_cleaning\clean_casualties.csv")
roads = pd.read_csv(r"C:\Users\shiva\OneDrive\Desktop\accident_analysis_project\data\Dataset_after_cleaning\clean_road_conditions.csv")

# Merge datasets
df = accidents.merge(vehicles, on='accident_id') \
              .merge(casualties, on='accident_id') \
              .merge(roads, on='accident_id')

print("\n📌 Dataset Overview")
print(df.info())

print("\n📌 Accident Count by Location")
print(df['location'].value_counts())

print("\n📌 Accidents by Time of Day")
print(df['time_of_day'].value_counts())

print("\n📌 Vehicle Type Distribution")
print(df['vehicle_type'].value_counts())

print("\n📌 Severity Distribution")
print(df['severity'].value_counts())

print("\n📌 Weather Impact")
print(df.groupby('weather')['severity'].value_counts())

print("\n📌 Driver Behavior")
print(df['driver_behavior'].value_counts())

print("\n📌 Traffic Conditions")
print(df['traffic'].value_counts())

print("\n📌 Road Conditions")
print(df['road_condition'].value_counts())