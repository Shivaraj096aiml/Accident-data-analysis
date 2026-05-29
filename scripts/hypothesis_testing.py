import pandas as pd
from scipy.stats import chi2_contingency

# Load data
accidents = pd.read_csv(r"C:\Users\shiva\OneDrive\Desktop\accident_analysis_project\data\Dataset_after_cleaning\clean_accidents.csv")
vehicles = pd.read_csv(r"C:\Users\shiva\OneDrive\Desktop\accident_analysis_project\data\Dataset_after_cleaning\clean_vehicles.csv")

# Merge
df = accidents.merge(vehicles, on='accident_id')

# -----------------------------
# Hypothesis 1: Weather vs Severity
# -----------------------------
print("\n🔹 Hypothesis 1: Weather affects severity")

table1 = pd.crosstab(df['weather'], df['severity'])

chi2, p, dof, expected = chi2_contingency(table1)

print("P-value:", p)

if p < 0.45:
    print("✅ Reject Null Hypothesis (Weather affects severity)")
else:
    print("❌ Fail to Reject Null Hypothesis")

# -----------------------------
# Hypothesis 2: Driver Behavior vs Severity
# -----------------------------
print("\n🔹 Hypothesis 2: Driver behavior affects severity")

table2 = pd.crosstab(df['driver_behavior'], df['severity'])

chi2, p, dof, expected = chi2_contingency(table2)

print("P-value:", p)

if p < 0.45:
    print("✅ Reject Null Hypothesis (Behavior impacts accidents)")
else:
    print("❌ No significant impact")

# -----------------------------
# Hypothesis 3: Traffic vs Severity
# -----------------------------
print("\n🔹 Hypothesis 3: Traffic affects severity")

table3 = pd.crosstab(df['traffic'], df['severity'])

chi2, p, dof, expected = chi2_contingency(table3)

print("P-value:", p)

if p < 0.05:
    print("✅ Traffic significantly affects accidents")
else:
    print("❌ No strong relation")