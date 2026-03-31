import pandas as pd 
import numpy as np
import chardet
from pathlib import Path
from openpyxl import workbook

file_path = "PBJ_Daily_Nurse_Staffing_Q2_2024.csv"
# it was giving me an enconding error. I had to get this script to change the encoding. 

# Read the first 1,000,000 bytes to guess the encoding
with open(file_path, 'rb') as f:
    raw_data = f.read(100000)
    result = chardet.detect(raw_data)
    encoding_guess = result['encoding']
    confidence = result['confidence']

print(f"Predicted Encoding: {encoding_guess}")
print(f"Confidence: {confidence * 100}%")

df = pd.read_csv("PBJ_Daily_Nurse_Staffing_Q2_2024.csv", encoding='latin1')
print("Shape:", df.shape)
df.head()

# 3. Data Analysis Task 
# 3.1 Understanding the dataset structure and schema 
print("\nUnderstanding the dataset structure and schema: ")
print(df.info())
print(df.columns)
print(df.head())


# 3.2 Identify key columns for grouping and analysis
print("\n Identify key columns for grouping and analysis:")

group_cols = ["PROVNUM", "PROVNAME", "CITY", "STATE", "COUNTY_NAME", "WorkDate"]
staffing_cols = ["Hrs_RN","Hrs_RN_ctr", "Hrs_LPN","Hrs_LPN_ctr","Hrs_CNA","Hrs_CNA_ctr","Hrs_NAtrn", "Hrs_MedAide"]
patient_col = "MDScensus"

# 3.3 Check for missing values
missing_values = df.isnull().sum().sort_values(ascending=False)
print("\nMISSING VALUES:")
print(missing_values[missing_values > 0])


# 3.4 Identify duplicate records 
duplicates = df.duplicated().sum() 
print("\nTOTAL DUPLICATE ROWS:", duplicates)

# 3.5 Detect ouliers in staffing hours 

staffing_summary = df[staffing_cols].describe()
print("\nstaffing_summary:")
print(staffing_summary)

"""
for col in staffing_cols: 
    print(f"\nOutliers check for {col}:")
    print("Max:", df[col].max())
    print("Min:", df[col].min())
"""

# 3.6 Convert date fields to proper datetime format 

# 3.6.1 Check a sample of the raw dates before conversion
print("Raw Date Samples:", df["WorkDate"].unique()[:5])

df["WorkDate"] = pd.to_datetime(df["WorkDate"].astype(str), format="%Y%m%d", errors="coerce")
df["Month_num"] = df["WorkDate"].dt.month
df["Month"] = df["WorkDate"].dt.month_name()


# 4. Data Cleaning 
clean_df = df.copy() 


# 4.1 Handle missing values where appropriate = (No missing Values checked on a previous step)
clean_df = clean_df.replace([np.inf, -np.inf], np.nan) 
clean_df = clean_df.dropna(subset=["PROVNUM"])
clean_df["PROVNUM"] = clean_df["PROVNUM"].astype(str).str.removesuffix(".0")
clean_df["PROVNUM"] = clean_df["PROVNUM"].str.zfill(6)
clean_df["PROVNUM"] = clean_df["PROVNUM"].str.strip()




print("\nData Clean up - Removing negative or zero values")
before = len(clean_df)
clean_df = clean_df[(clean_df[staffing_cols] > 0).any(axis=1)]
after = len(clean_df)
print(f"After removing negative staffing rows: {after} rows left, removed {before - after}")
before = len(clean_df)
clean_df = clean_df[clean_df["MDScensus"] > 0]
after = len(clean_df)
print(f"After removing negative MDScensus rows: {after} rows left, removed {before - after}")

# 4.2 Remove duplicate rows = (No duplicated rows checked on a previous step)
# 4.3 Ensure WorkDate is in datetime format =  (Done = datetime64[ns])
# 4.4 Verify that staffing hours are numeric(Confirmed as per print(df.info()) all are float64.
# 4.5 Check unrealistic staffing values (extreme outliers) Check: 


# 4.6 Create derived columns for total nurse hours
nurse_ratio_cols = ["Hrs_RN", "Hrs_LPN", "Hrs_CNA"]  
clean_df["Total Nurse Hours"] = clean_df[nurse_ratio_cols].sum(axis=1)
print("\n4.6 Total Nurse Hours ")
print(clean_df["Total Nurse Hours"].sort_values(ascending=False).head())


# 5.0 Key Metrics to Calculate 
# 5.1 Nurse-to-Patient Ratio
clean_df["Nurse-to-Patient Ratio"] = (clean_df["Total Nurse Hours"]/clean_df[patient_col])
   
print("5.1_Nurse-to-Patient Ratio:") 
print(clean_df["Nurse-to-Patient Ratio"].sort_values(ascending=False))

# 5.2 Total Nurse Hours (Total nurse hours worked per hospital per month. Group by: Hospital, State, Month).

monthly_nurse_hours = ( 
    clean_df
    .groupby(["PROVNUM","PROVNAME", "STATE", "Month"])["Total Nurse Hours"]
    .sum()
    .reset_index()
    .sort_values("Total Nurse Hours", ascending=False)
    
)
print("\n5.2 Total nurse hours worked per hospital per month")
print(monthly_nurse_hours.head())

# 5.3 Contract vs Permanent(Non-Contract) Staff Ratio

contract_cols = ["Hrs_RN_ctr", "Hrs_LPN_ctr", "Hrs_CNA_ctr"]

nurse_cols  = ["Hrs_RN_emp", "Hrs_LPN_emp","Hrs_CNA_emp",
                 "Hrs_NAtrn", "Hrs_MedAide"]

clean_df["Total Contract Hours"] = clean_df[contract_cols].sum(axis=1) 
clean_df["Total Nurse Hours"] = clean_df[nurse_cols ].sum(axis=1) 

clean_df["Contract Ratio"] = (
    (clean_df["Total Contract Hours"]/clean_df["Total Nurse Hours"])
     .replace([np.inf, -np.inf], np.nan)
)
print("\n5.3_Contract Ratio")
print(clean_df["Contract Ratio"].sort_values(ascending=False)) 

# 5.4 Average Patient Census (Average number of patients per hospital or per state).

avg_census_hospital = (
    clean_df
    .groupby(["PROVNUM","PROVNAME","STATE"])["MDScensus"]
    .mean()
    .reset_index(name="Average Patient Census")
    .sort_values(by ="Average Patient Census", ascending=False)
)
print("\n5.4  Average number of patients per hospital")
print(avg_census_hospital)

avg_census_state = (
    clean_df
    .groupby("STATE")["MDScensus"]
    .mean()
    .reset_index(name="Average Patient Census")
    .sort_values(by ="Average Patient Census", ascending=False)
)
print("\n5.4  Average number of patients per state ")
print(avg_census_state.head())

# 5.5 Hospitals with Highest Staffing Hours. (Identify hospitals with the highest total staffing hours).
clean_df["total_staffing_hours"] = clean_df[staffing_cols].sum(axis=1)


hospital_high_hours = (
    clean_df
    .groupby(["PROVNUM","PROVNAME"])["total_staffing_hours"]
    .sum()
    .sort_values(ascending=False)
    .reset_index()
    
)
print("\nIdentify hospitals with the highest total staffing hours")
print(hospital_high_hours)

# 6. Analytical Questions. 
# 6.1 What is the relationship between nurse staffing levels and patient census? 

staffing_vs_census = (
    clean_df
    .groupby(["PROVNUM","PROVNAME", "Month_num"], as_index=False)
    .agg({
        "total_staffing_hours": "sum",
        "MDScensus": "mean"
    })
)

correlation = staffing_vs_census["total_staffing_hours"].corr(staffing_vs_census["MDScensus"])

print("\n6.1 What is the relationship between nurse staffing levels and patient census:")
print("Correlation", correlation)


# 6.3 What are the average staffing levels by state? 

hospital_staffing = (
    clean_df
    .groupby(["STATE","PROVNUM","PROVNAME"], as_index=False)["total_staffing_hours"]
    .sum()
)

average_staffing_state = (
    hospital_staffing
    .groupby("STATE")["total_staffing_hours"]
    .mean()
    .sort_values(ascending=False)
    .reset_index()
)
print("\n6.3 average staffing levels by state:")
print(average_staffing_state.head())

# 6.4 Which facilities have the lowest nurse-to-patient coverage?


facility_coverage = (
    clean_df
    .groupby(["PROVNUM","PROVNAME"], as_index=False)
    .agg({
        "total_staffing_hours": "sum",
        "MDScensus": "sum"
    })
)

facility_coverage["Coverage"] = ( facility_coverage["total_staffing_hours"] /facility_coverage["MDScensus"])

facility_coverage = (
    facility_coverage
    .replace([np.inf, -np.inf], np.nan)
    .sort_values(by="Coverage", ascending=False)
    .reset_index()
    
)
print("\n6.4 Which facilities have the lowest nurse-to-patient coverage")
print(facility_coverage[["PROVNUM","PROVNAME", "Coverage"]].head(10))
print(facility_coverage) 



# 6.5 Are certain states relying more on contract nurses? 
states_relationship = ( 
    clean_df
    .groupby("STATE")
    .agg({
        "Total Nurse Hours": "sum",
        "Total Contract Hours": "sum"
    })
    .reset_index()
)
states_relationship["Contract Ratio"] = (
        states_relationship["Total Contract Hours"]/states_relationship["Total Nurse Hours"]
        ).replace([np.inf, -np.inf], np.nan)
print("\n6.5 Are certain states relying more on contract nurses")
print("\nstates_relationship")
print(states_relationship.sort_values(by="Contract Ratio", ascending=False).head(5))



clean_df.to_csv("clean_Healthcare_data_BI.csv", index=False, quoting=1)


print(clean_df.info())