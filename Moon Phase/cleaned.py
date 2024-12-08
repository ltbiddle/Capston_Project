import pandas as pd

# Read the CSV file
df = pd.read_csv("input.csv")

# Ensure the column containing dates is in datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Change the date format
# For example, converting to 'YYYY-MM-DD'
df['Date'] = df['Date'].dt.strftime('%Y-%m-%d')

# Save the updated DataFrame back to a CSV
df.to_csv("output.csv", index=False)

print("Date format updated and saved to output.csv")