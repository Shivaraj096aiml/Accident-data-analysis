import pandas as pd

df = pd.read_csv(r"C:\Users\shiva\OneDrive\Desktop\accident_analysis_project\Dataset\vehicles.csv")

# Remove duplicates
df = df.drop_duplicates()

# Handle missing values
df = df.dropna(subset=['vehicle_id', 'accident_id'])

# Fix data types
df['driver_age'] = pd.to_numeric(df['driver_age'], errors='coerce')

# Remove invalid ages
df = df[(df['driver_age'] >= 18) & (df['driver_age'] <= 80)]

# Standardize text
df['vehicle_type'] = df['vehicle_type'].str.capitalize().str.strip()
df['driver_behavior'] = df['driver_behavior'].str.title().str.strip()

# Save cleaned data
df.to_csv("clean_vehicles.csv", index=False)

print("✅ Vehicles cleaned")