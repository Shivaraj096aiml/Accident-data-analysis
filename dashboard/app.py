import streamlit as st
import pandas as pd

st.set_page_config(page_title="Accident Dashboard", layout="wide")



# -----------------------------
# LOAD DATA
# -----------------------------
@st.cache_data
def load_data():
    accidents = pd.read_csv(r"C:\Users\shiva\OneDrive\Desktop\accident_analysis_project\data\Dataset_after_cleaning\clean_accidents.csv")
    vehicles = pd.read_csv(r"C:\Users\shiva\OneDrive\Desktop\accident_analysis_project\data\Dataset_after_cleaning\clean_vehicles.csv")
    casualties = pd.read_csv(r"C:\Users\shiva\OneDrive\Desktop\accident_analysis_project\data\Dataset_after_cleaning\clean_casualties.csv")
    roads = pd.read_csv(r"C:\Users\shiva\OneDrive\Desktop\accident_analysis_project\data\Dataset_after_cleaning\clean_road_conditions.csv")

    df = accidents.merge(vehicles, on='accident_id') \
                  .merge(casualties, on='accident_id') \
                  .merge(roads, on='accident_id')
    return df

df = load_data()

# -----------------------------
# TITLE
# -----------------------------
st.markdown("<h1 style='text-align: center; color: #FF4B4B;'>🚦 Accident Analysis Dashboard</h1>", unsafe_allow_html=True)
st.markdown("---")

# -----------------------------
# FILTERS
# -----------------------------
st.sidebar.title("🔍 Filter Panel")

location = st.sidebar.multiselect("📍 Location", df['location'].unique())
weather = st.sidebar.multiselect("🌧️ Weather", df['weather'].unique())
vehicle = st.sidebar.multiselect("🚗 Vehicle Type", df['vehicle_type'].unique())

filtered_df = df.copy()

if location:
    filtered_df = filtered_df[filtered_df['location'].isin(location)]

if weather:
    filtered_df = filtered_df[filtered_df['weather'].isin(weather)]

if vehicle:
    filtered_df = filtered_df[filtered_df['vehicle_type'].isin(vehicle)]

# -----------------------------
# KPI
# -----------------------------
st.subheader("📊 Key Metrics")

col1, col2, col3 = st.columns(3)

col1.metric("🚗 Total Accidents", len(filtered_df[['accident_id']].drop_duplicates()))
col2.metric("💀 Fatal Accidents", len(filtered_df[filtered_df['severity'] == 'Fatal'][['accident_id']].drop_duplicates()))
col3.metric("🧍 Casualties", len(filtered_df))

# -----------------------------
# FIXED DATA FOR CHARTS
# -----------------------------
unique_df = filtered_df.drop_duplicates(subset=['accident_id'])

# -----------------------------
# CHARTS
# -----------------------------
st.subheader("📈 Analysis")

col1, col2 = st.columns(2)

with col1:
    st.write("### Severity Distribution")
    st.bar_chart(unique_df['severity'].value_counts())

with col2:
    st.write("### Vehicle Type")
    st.bar_chart(filtered_df['vehicle_type'].value_counts())

col3, col4 = st.columns(2)

with col3:
    st.write("### Time of Day")
    st.bar_chart(unique_df['time_of_day'].value_counts())

with col4:
    st.write("### Weather Conditions")
    st.bar_chart(unique_df['weather'].value_counts())

# -----------------------------
# DRIVER BEHAVIOR
# -----------------------------
st.subheader("🚗 Driver Behavior Impact")
st.bar_chart(filtered_df['driver_behavior'].value_counts())

# -----------------------------
# ROAD CONDITIONS
# -----------------------------
st.subheader("🛣️ Road Conditions")
st.bar_chart(filtered_df['road_condition'].value_counts())

# -----------------------------
# INSIGHTS
# -----------------------------
st.subheader("💡 Insights")

if not filtered_df.empty:
    top_vehicle = filtered_df['vehicle_type'].value_counts().idxmax()
    top_location = unique_df['location'].value_counts().idxmax()

    st.success(f"🚗 Most accidents involve: {top_vehicle}")
    st.info(f"📍 Most affected location: {top_location}")

    if unique_df['severity'].value_counts().idxmax() == "Fatal":
        st.warning("⚠️ High number of fatal accidents detected!")

# -----------------------------
# DATA PREVIEW (ADVANCED)
# -----------------------------
st.subheader("📄 Data Preview")

columns = st.multiselect("Select columns", filtered_df.columns, default=filtered_df.columns)

search = st.text_input("Search data")

temp_df = filtered_df[columns]

if search:
    temp_df = temp_df[temp_df.astype(str).apply(lambda x: x.str.contains(search, case=False)).any(axis=1)]

num_rows = st.slider("Rows to display", 5, 100, 10)

st.dataframe(temp_df.head(num_rows))

# -----------------------------
# DOWNLOAD
# -----------------------------
st.subheader("⬇️ Download Data")

csv = filtered_df.to_csv(index=False).encode('utf-8')

st.download_button(
    label="Download CSV",
    data=csv,
    file_name="filtered_accidents.csv",
    mime="text/csv",
)