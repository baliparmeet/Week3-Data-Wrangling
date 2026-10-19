
import pandas as pd

# Load the dataset
df = pd.read_csv("data.csv")

# Display the first 5 rows
print(df.head())

# Display the dataset information
print(df.info())

# Check the number of rows and columns
print(df.shape)

# Check missing values in each column
print("\nMissing values:")
print(df.isnull().sum())

# Display rows containing missing values
print("\nRows with missing values:")
print(df[df.isnull().any(axis=1)])

# Fill missing Calories with the average
df["Calories"] = df["Calories"].fillna(df["Calories"].mean())

# Remove rows where Date is missing
df = df.dropna(subset=["Date"])

# Check missing values again
print("\nMissing values after cleaning:")
print(df.isnull().sum())

# Check the new dataset size
print("\nDataset shape after cleaning:")
print(df.shape)

# Check for duplicate rows
print("\nNumber of duplicate rows:")
print(df.duplicated().sum())

# Remove duplicate rows
df = df.drop_duplicates()

# Check duplicates again
print("\nDuplicates after cleaning:")
print(df.duplicated().sum())

# Check the final dataset size
print("\nFinal dataset shape:")
print(df.shape)

# Filter workouts with more than 400 calories
high_calories = df[df["Calories"] > 400]

print("\nWorkouts with more than 400 calories:")
print(high_calories)

# Create a new column called Intensity
df["Intensity"] = df["Pulse"].apply(
    lambda pulse: "High" if pulse >= 100 else "Normal"
)

# Display the updated dataset
print("\nDataset with workout intensity:")
print(df[["Pulse", "Intensity"]].head(10))

import matplotlib.pyplot as plt

# Count workouts in each intensity category
intensity_counts = df["Intensity"].value_counts()

# Create a bar chart
intensity_counts.plot(kind="bar")

plt.title("Number of Workouts by Intensity")
plt.xlabel("Intensity")
plt.ylabel("Number of Workouts")
plt.xticks(rotation=0)

plt.tight_layout()
plt.show()

# Save the cleaned dataset
df.to_csv("cleaned_data.csv", index=False)

print("\nCleaned dataset saved successfully!")
