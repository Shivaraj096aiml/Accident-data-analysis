import pandas as pd

df = pd.read_csv(r"C:\Users\shiva\OneDrive\Desktop\accident_analysis_project\Dataset\road_conditions.csv")

# Remove duplicates
df = df.drop_duplicates()

# Handle missing values
df = df.dropna(subset=['road_id', 'accident_id'])

# Standardize text
df['road_type'] = df['road_type'].str.title().str.strip()
df['lighting'] = df['lighting'].str.title().str.strip()
df['road_condition'] = df['road_condition'].str.title().str.strip()

# Save cleaned data
df.to_csv("clean_road_conditions.csv", index=False)

print("✅ Road conditions cleaned")