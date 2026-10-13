
import pandas as pd
import matplotlib.pyplot as plt

# Create inventory data for 10 products
data = {
    "Product": [
        "Cola", "Chips", "Milk", "Biscuits", "Juice",
        "Yogurt", "Water", "Cookies", "Cheese", "Energy Drink"
    ],
    "Category": [
        "beverages ", "SNACKS", " Dairy", "Snacks", "beverages",
        "DAIRY ", " beverages", " snacks ", "Dairy", "BEVERAGES"
    ],
    "Price": [
        "Rs. 1,250", "Rs. 90", "Rs. 450", "Rs. 120", "Rs. 1,800",
        "Rs. 300", "Rs. 60", "Rs. 200", "Rs. 700", "Rs. 2,000"
    ],
    "Stock": [40, 120, 60, 90, 35, 50, 150, 75, 30, 25]
}

df = pd.DataFrame(data)

# Clean category names
df["Category"] = df["Category"].str.strip().str.title()

# Remove currency prefix and commas, then convert prices to numbers
df["Price"] = (
    df["Price"]
    .str.replace("Rs. ", "", regex=False)
    .str.replace(",", "", regex=False)
    .astype(float)
)

# Encode categories as numeric codes
df["Category_Code"] = df["Category"].astype("category").cat.codes

print("Cleaned Inventory:")
print(df)

# Calculate average price and total stock per category
average_price = df.groupby("Category")["Price"].mean()
total_stock = df.groupby("Category")["Stock"].sum()

# Create two plots side by side
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

axes[0].bar(average_price.index, average_price.values)
axes[0].set_title("Average Price by Category")
axes[0].set_xlabel("Category")
axes[0].set_ylabel("Average Price (Rs.)")
axes[0].tick_params(axis="x", rotation=20)

axes[1].pie(
    total_stock.values,
    labels=total_stock.index,
    autopct="%1.1f%%",
    startangle=90
)
axes[1].set_title("Share of Total Stock by Category")

plt.tight_layout()
plt.savefig("inventory_plots.png")
plt.show()

print("Saved inventory_plots.png")