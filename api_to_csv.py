
import requests
import pandas as pd

# Fetch data from a public API
url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(url, timeout=30)
response.raise_for_status()

# Convert JSON response to a DataFrame
data = response.json()
df = pd.DataFrame(data)

# Save data as CSV
df.to_csv("api_data.csv", index=False)

print("API data extracted successfully!")
print(df.head())
print("Total records:", len(df))
