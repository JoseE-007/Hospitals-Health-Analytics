# Healthcare Staffing Analytics

## Overview
End-to-end analysis of nurse staffing data to evaluate operational efficiency, staffing coverage, and patient load across U.S. healthcare facilities.
The project transforms raw CMS PBJ data into actionable metrics and a Power BI dashboard for decision-making.

## Objective
- Evaluate nurse staffing vs patient demand
- Identify under-resourced facilities
- Analyze contract staff dependency
- Monitor staffing trends over time

## Dataset
- Source: PBJ Daily Nurse Staffing (Q2 2024)
- Grain: Daily staffing per facility

Key fields:
- Facility: PROVNUM, PROVNAME, STATE
- Time: WorkDate
- Staffing: RN, LPN, CNA hours (emp vs contract)
- Patients: MDScensus

## Process

### 1. Data Preparation
- Encoding detection & correction
- Datetime conversion
- Data type standardization
- Filtering invalid rows (negative / zero values)

### 2. Feature Engineering
- Total Nurse Hours
- Nurse-to-Patient Ratio
- Contract Ratio
- Monthly aggregations

### 3. Analysis
- Correlation between staffing and patient census
- State-level staffing comparison
- Facility-level coverage analysis
- Contract staffing dependency


## Key Metrics

- **Nurse-to-Patient Ratio**  
  (RN + LPN + CNA Hours) / Patient Census  

- **Total Staffing Hours**  
  Aggregated by hospital and state  

- **Contract Ratio**  
  Contract Hours / Total Nurse Hours  

- **Average Patient Census**  
  Facility and state level  

## Dashboard (Power BI)

### Staffing Overview
- Nurse hours by hospital  
- Staffing comparison by state  
- Contract vs employed ratio  

### Patient Load
- Patient census trend  
- Nurse-to-patient ratio trend  

### Operational Insights
- Top 10 busiest hospitals  
- Lowest staffing coverage facilities  

## Key Insights

- Weak negative correlation between staffing and patient census → potential inefficiency
- High variation in staffing across states
- Some facilities significantly under-resourced
- Contract staff reliance varies widely by state

## Tech Stack
- Python (Pandas, NumPy)
- Data Cleaning & EDA
- Power BI (Visualization)


## Project Structure
├── data/
├── notebooks/
├── scripts/
│ └── Clipboard_Health_Analytics.py
├── dashboard/
├── README.md
├── requirements.txt

Source file is over 300mb, ping me in case you need it. 

## Author 
JEF_007 
