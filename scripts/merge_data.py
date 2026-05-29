import pandas as pd

acc = pd.read_csv(r"C:\Users\shiva\OneDrive\Desktop\accident_analysis_project\Dataset_after_cleaning\clean_accidents.csv")
veh = pd.read_csv(r"C:\Users\shiva\OneDrive\Desktop\accident_analysis_project\Dataset_after_cleaning\clean_vehicles.csv")
cas = pd.read_csv(r"C:\Users\shiva\OneDrive\Desktop\accident_analysis_project\Dataset_after_cleaning\clean_casualties.csv")
road = pd.read_csv(r"C:\Users\shiva\OneDrive\Desktop\accident_analysis_project\Dataset_after_cleaning\clean_road_conditions.csv")

# Merge all tables
df = acc.merge(veh, on='accident_id', how='left') \
        .merge(cas, on='accident_id', how='left') \
        .merge(road, on='accident_id', how='left')

print(df.head())