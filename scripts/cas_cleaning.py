import pandas as pd

df = pd.read_csv(r"C:\Users\shiva\OneDrive\Desktop\accident_analysis_project\Dataset\casualties.csv")

# Remove duplicates
df = df.drop_duplicates()

# Handle missing values
df = df.dropna(subset=['casualty_id', 'accident_id'])

# Fix data types
df['age'] = pd.to_numeric(df['age'], errors='coerce')

# Remove invalid ages
df = df[(df['age'] >= 0) & (df['age'] <= 100)]

# Standardize text
df['injury_type'] = df['injury_type'].str.capitalize().str.strip()

# Save cleaned data
df.to_csv("clean_casualties.csv", index=False)

print("✅ Casualties cleaned")