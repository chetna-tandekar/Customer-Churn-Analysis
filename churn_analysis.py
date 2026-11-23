import pandas as pd

#Load the customer churn dataset
df = pd.read_csv(r"D:\OneDrive\Desktop\Customer churn analysis folder\Telco- Customer- churn.csv")

#Display the first 5 row
print(df.head())

# Check dataset dimensions
print("nDataset Shape:")
print(df.shape)

#Check columns names
print("\nColumn Names:")
print(df.columns.tolist())

# Check dataset information
print("\nDataset Information:")
df.info()

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Check blank values in TotalChanges
print("\nBlank TotalCharges:")
print(df["TotalCharges"].str.strip().eq("").sum())

# Inspect customers with blank Totalcharges
blank_customers = df[
    df["TotalCharges"].str.strip().eq("")
]

print("\nCustomers with blank TotalCharges:")
print(
    blank_customers[
        ["customerID", "tenure", "MonthlyCharges", "TotalCharges", "Churn"]
    ]
)

#Clean TotalCharges column
df["TotalCharges"] = df["TotalCharges"].str.strip()

# Convert Total Charges from text to numeric
df["TotalCharges"] = pd.to_numeric(
    df["TotalCharges"], errors="coerce"
)

# Replace missing Totalcharges with 0
df["TotalCharges"] = df["TotalCharges"].fillna(0)

# Verify cleaning
print("\nAfter Cleaning:")
print(df["TotalCharges"].isnull().sum())
print(df["TotalCharges"].dtype)

# Save cleaned dataset
df.to_csv("Telco-Customer-Churn-Cleaned.csv", index=False)
print("\nCleaned dataset saved successfully!")

# Exploratory Data Analysis (EDA)

# Count customers who left and stayed 
churn_counts = df["Churn"].value_counts()

print("\nCustomer Churn Count:")
print(churn_counts)

# Calculate churn percentage
churn_percentage = (
    df["Churn"].value_counts(normalize=True) * 100
)

print("\nCustomer Churn Percentage:")
print(churn_percentage.round(2))

# Churn analysis by contract type

contract_churn = pd.crosstab(
    df["Contract"],
    df["Churn"],
    normalize= "index"
) * 100

print("\nChurn Percentage by Contract:")
print(contract_churn.round(2))

# Churn Percentage by Internet Service

print("\nChurn Percentage by Internet Service:")

internet_churn = pd.crosstab(
    df['InternetService'],
    df['Churn'],
    normalize='index'
) * 100

print(internet_churn.round(2))

import matplotlib.pyplot as plt

# Churn percentage by contract
churn_by_contract = pd.crosstab(
    df['Contract'],
    df['Churn'],
    normalize='index'
) * 100

churn_by_contract["Yes"].plot(
    kind='bar',
    title='Customer Churn by Contract Type'
)

plt.xlabel('Contract Type')
plt.ylabel('Churn Percentage (%)')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# Churn percentage by Internet Service

churn_by_internet = pd.crosstab(
    df['InternetService'],
    df['Churn'],
    normalize='index'
) * 100

churn_by_internet['Yes'].plot(
    kind='bar',
    title='Customer Churn by Internet Service'
)

plt.xlabel('Internet Service')
plt.ylabel('Churn Percentage (%)')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# Churn percentage by Pyment Method 

churn_by_payment = pd.crosstab(
    df['PaymentMethod'],
    df['Churn'],
    normalize='index'
) * 100

churn_by_payment['Yes'].plot(
    kind='bar',
    title='Customer Churn by Payment Method'
)

plt.xlabel('Payment Method')
plt.ylabel('Churn Percentage(%)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Churn percentage by tech support

churn_by_support = pd.crosstab(
    df['TechSupport'],
    df['Churn'],
    normalize='index'
) * 100

churn_by_support['Yes'].plot(
    kind='bar',
    title='Customer Churn by Tech Support'
)

plt.xlabel('Tech Support')
plt.ylabel('Churn Percentage (%)')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

#  Customer Churn by Tenure

tenure_churn = df.groupby("Churn")["tenure"].mean()

print("\nAverage Tenure by Churn Status:")
print(tenure_churn.round(2))

tenure_churn.plot(
    kind="bar",
    title="Average Customer Tenure by Churn Status"
)

plt.xlabel("Customer Churn")
plt.ylabel("Average Tenure (Months)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# Customer Analysis Summary

print("\nCUSTOMER ANALYSIS SUMMARY")

print("\nAverage Monthly Charges:")
print(df["MonthlyCharges"].mean().round(2))

print("\nAverage Total Charges:")
print(df["TotalCharges"].mean().round(2))

print("\nAverage Tenure:")
print(df["tenure"].mean().round(2))

print("\nChurn by Senior Citizen:")
senior_churn = pd.crosstab(
    df["SeniorCitizen"],
    df["Churn"],
    normalize="index"
) * 100

print(senior_churn.round(2))