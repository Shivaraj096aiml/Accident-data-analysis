import pandas as pd

# Load data
df = pd.read_csv(r"C:\Users\shiva\OneDrive\Desktop\accident_analysis_project\Dataset\accidents.csv")

# Remove duplicates
df = df.drop_duplicates()

# Convert date & time
df['date'] = pd.to_datetime(df['date'], errors='coerce')
df['time'] = pd.to_datetime(df['time'], format='%H:%M:%S', errors='coerce').dt.time

# Handle missing values
df = df.dropna(subset=['accident_id', 'date', 'location'])

# Standardize text columns
df['location'] = df['location'].str.title().str.strip()
df['state'] = df['state'].str.title().str.strip()
df['weather'] = df['weather'].str.capitalize().str.strip()
df['severity'] = df['severity'].str.capitalize().str.strip()

# Save cleaned file
df.to_csv("clean_accidents.csv", index=False)

print("✅ Accidents cleaned")