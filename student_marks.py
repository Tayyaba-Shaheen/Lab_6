
import pandas as pd
import matplotlib.pyplot as plt

# Create the student dataset
data = {
    "Name": [
        " ali", "SARA ", "bilal", " Ayesha",
        "HAMZA", "zain ", "Noor", " usman "
    ],
    "Marks": ["72", "85", "absent", "64", "90", "78", "81", "69"]
}

df = pd.DataFrame(data)

# Clean names
df["Name"] = df["Name"].str.strip().str.title()

# Convert marks to numbers; "absent" becomes NaN
df["Marks"] = pd.to_numeric(df["Marks"], errors="coerce")

# Fill missing marks with the mean of the other marks
mean_marks = df["Marks"].mean()
df["Marks"] = df["Marks"].fillna(mean_marks)

print("Cleaned Student Data:")
print(df)

# Draw and save the bar plot
plt.figure(figsize=(8, 5))
plt.bar(df["Name"], df["Marks"])
plt.title("Student Marks")
plt.xlabel("Student Name")
plt.ylabel("Marks")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("marks_bar.png")
plt.show()

print("Saved marks_bar.png")