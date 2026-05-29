import pandas as pd
import random
from faker import Faker

fake = Faker()

# -----------------------
# CONFIG
# -----------------------
NUM_RECORDS = 5000

locations = ["Visakhapatnam", "Bangalore", "Chennai", "Mumbai", "Delhi", "Hyderabad"]

states = {
    "Visakhapatnam": "Andhra Pradesh",
    "Bangalore": "Karnataka",
    "Chennai": "Tamil Nadu",
    "Mumbai": "Maharashtra",
    "Delhi": "Delhi",
    "Hyderabad": "Telangana"
}

vehicle_types = ["Car", "Bike", "Truck", "Bus", "Auto", "Van", "Bicycle"]
vehicle_condition = ["Good", "Average", "Poor"]

severity_levels = ["Minor", "Serious", "Fatal"]
weather_types = ["Clear", "Rain", "Fog", "Storm", "Drizzle", "Cloudy"]

road_types = ["Highway", "City Road", "Rural Road", "Expressway"]
lighting_types = ["Daylight", "Street Light", "No Light", "Dim Light"]

driver_behavior = ["Normal", "Overspeeding", "Drunk Driving", "Distracted", "Fatigue"]
traffic_conditions = ["Low", "Moderate", "Heavy"]

road_condition = ["Dry", "Wet", "Under Construction", "Damaged"]
response_time = ["<10 min", "10-20 min", "20-30 min", ">30 min"]

passenger_count = list(range(1, 6))

# -----------------------
# HELPER FUNCTION
# -----------------------
def get_time_of_day(hour):
    if 5 <= hour < 12:
        return "Morning"
    elif 12 <= hour < 17:
        return "Afternoon"
    elif 17 <= hour < 21:
        return "Evening"
    else:
        return "Night"

# -----------------------
# ACCIDENTS TABLE
# -----------------------
accidents = []

for i in range(1, NUM_RECORDS + 1):
    location = random.choice(locations)
    time_obj = fake.time_object()
    hour = time_obj.hour

    accidents.append([
        i,
        fake.date_between(start_date='-1y', end_date='today'),
        time_obj,
        get_time_of_day(hour),
        location,
        states[location],
        random.choice(severity_levels),
        random.choice(weather_types),
        random.choice(traffic_conditions)
    ])

accidents_df = pd.DataFrame(accidents, columns=[
    "accident_id", "date", "time", "time_of_day",
    "location", "state", "severity", "weather", "traffic"
])

# -----------------------
# VEHICLES TABLE
# -----------------------
vehicles = []

for i in range(1, NUM_RECORDS + 1):
    vehicles.append([
        f"V{i}",
        i,
        random.choice(vehicle_types),
        random.choice(vehicle_condition),
        random.choice(driver_behavior),
        random.randint(18, 65),
        random.choice(passenger_count)
    ])

vehicles_df = pd.DataFrame(vehicles, columns=[
    "vehicle_id", "accident_id", "vehicle_type",
    "vehicle_condition", "driver_behavior",
    "driver_age", "passenger_count"
])

# -----------------------
# CASUALTIES TABLE
# -----------------------
casualties = []

for i in range(1, NUM_RECORDS + 1):
    casualties.append([
        f"C{i}",
        i,
        random.choice(["Minor", "Serious", "Fatal", "None"]),
        random.randint(1, 75)
    ])

casualties_df = pd.DataFrame(casualties, columns=[
    "casualty_id", "accident_id", "injury_type", "age"
])

# -----------------------
# ROAD CONDITIONS TABLE
# -----------------------
roads = []

for i in range(1, NUM_RECORDS + 1):
    roads.append([
        f"R{i}",
        i,
        random.choice(road_types),
        random.choice(lighting_types),
        random.choice(road_condition),
        random.choice(response_time)
    ])

roads_df = pd.DataFrame(roads, columns=[
    "road_id", "accident_id", "road_type",
    "lighting", "road_condition", "response_time"
])

# -----------------------
# SAVE FILES
# -----------------------
accidents_df.to_csv("accidents.csv", index=False)
vehicles_df.to_csv("vehicles.csv", index=False)
casualties_df.to_csv("casualties.csv", index=False)
roads_df.to_csv("road_conditions.csv", index=False)

print("✅ 5000-row REALISTIC dataset generated successfully!")