
import pandas as pd
import matplotlib.pyplot as plt

# Create a 15-day weather dataset
data = {
    "Date": [
        "2026-06-01", "2026-06-02", "2026-06-03",
        "2026-06-04", "2026-06-05", "2026-06-06",
        "2026-06-07", "2026-06-08", "2026-06-09",
        "2026-06-10", "2026-06-11", "2026-06-12",
        "2026-06-13", "2026-06-14", "2026-06-15"
    ],
    "City": [
        " lahore", "LAHORE ", "Karachi", " islamabad",
        "KARACHI", "Lahore ", "ISLAMABAD", "Karachi ",
        "lahore", "Islamabad ", "KARACHI", "Lahore",
        " islamabad ", "Karachi", "LAHORE"
    ],
    "Temperature": [
        "32C", "34C", "30C", "28C", "31C",
        "35C", "27C", "29C", "33C", "26C",
        "32C", "36C", "28C", "30C", "34C"
    ],
    "Humidity": [
        55, 50, None, 65, 60, 45, 70, None,
        52, 72, 58, None, 68, 62, 48
    ],
    "Condition": [
        "sunny", " Sunny ", "CLOUDY", " Rainy", "cloudy ",
        "SUNNY", "rainy", "Cloudy", " sunny ", "RAINY",
        "Sunny", "CLOUDY ", "rainy", "cloudy", "SUNNY"
    ]
}

df = pd.DataFrame(data)

# Add one exact duplicate row
df = pd.concat([df, df.iloc[[2]]], ignore_index=True)

# Clean text columns
df["City"] = df["City"].str.strip().str.title()
df["Condition"] = df["Condition"].str.strip().str.title()

# Convert temperature strings such as "32C" into numbers
df["Temperature"] = (
    df["Temperature"].str.replace("C", "", regex=False).astype(float)
)

# Convert dates into datetime values
df["Date"] = pd.to_datetime(df["Date"])

# Remove duplicate rows
df = df.drop_duplicates().copy()
print("Rows after dropping duplicates:", len(df))

# Fill missing humidity with the median
humidity_median = df["Humidity"].median()
df["Humidity"] = df["Humidity"].fillna(humidity_median)
print("Missing Humidity filled with median:", humidity_median)

# One-hot encode the Condition column
df_encoded = pd.get_dummies(
    df, columns=["Condition"], dtype=int
)

print("\nEncoded condition columns:")
condition_columns = [
    column for column in df_encoded.columns
    if column.startswith("Condition_")
]
print(df_encoded[condition_columns].head())

# Calculate correlation
correlation = df["Temperature"].corr(df["Humidity"])
print("\nCorrelation (Temperature, Humidity):", round(correlation, 3))

# Count each weather condition
condition_counts = df["Condition"].value_counts()
print("\nCondition counts:")
print(condition_counts)

# Create a 2 x 2 weather dashboard
fig, axes = plt.subplots(2, 2, figsize=(12, 9))

# 1. Temperature over time
axes[0, 0].plot(
    df["Date"], df["Temperature"], marker="o"
)
axes[0, 0].set_title("Temperature Over Time")
axes[0, 0].set_xlabel("Date")
axes[0, 0].set_ylabel("Temperature (C)")
axes[0, 0].tick_params(axis="x", rotation=45)

# 2. Temperature vs Humidity
axes[0, 1].scatter(df["Temperature"], df["Humidity"])
axes[0, 1].set_title("Temperature vs Humidity")
axes[0, 1].set_xlabel("Temperature (C)")
axes[0, 1].set_ylabel("Humidity")

# 3. Weather condition pie chart
axes[1, 0].pie(
    condition_counts.values,
    labels=condition_counts.index,
    autopct="%1.1f%%",
    startangle=90
)
axes[1, 0].set_title("Weather Conditions")

# 4. Temperature histogram
axes[1, 1].hist(
    df["Temperature"], bins=6, edgecolor="black"
)
axes[1, 1].set_title("Temperature Distribution")
axes[1, 1].set_xlabel("Temperature (C)")
axes[1, 1].set_ylabel("Number of Days")

fig.suptitle("Weather Overview", fontsize=16)
plt.tight_layout()
plt.savefig("weather_dashboard.png")
plt.show()

print("Saved weather_dashboard.png")