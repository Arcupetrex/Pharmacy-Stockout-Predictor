import pandas as pd

# Step 1: Read the CSV file containing pharmacy stock data.
# The CSV file is expected to have the columns: 'drug_name', 'stock_level', 'sales_per_week'.
data = pd.read_csv("pharmacy_stock.csv")

# Step 2: Calculate the predicted stock after 2 weeks.
# We assume that sales_per_week remains constant over the next two weeks.
# Predicted remaining stock = current stock - (2 * sales_per_week)
data["predicted_stock"] = data["stock_level"] - (2 * data["sales_per_week"])

# Step 3: Identify the drugs that will run out.
# A drug is predicted to run out if its predicted_stock is less than or equal to 0.
drugs_to_reorder = data[data["predicted_stock"] <= 0]

# Step 4: Print the results.
print("Drugs predicted to run out in the next 2 weeks:")
print(drugs_to_reorder[["drug_name", "stock_level", "sales_per_week", "predicted_stock"]])

# Optional: Save the list of drugs that need to be reordered to a new CSV file.
drugs_to_reorder.to_csv("drugs_to_reorder.csv", index=False)