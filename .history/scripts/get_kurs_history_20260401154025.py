import requests
import pandas as pd

url = "https://api.frankfurter.app/2021-01-01..2026-01-01?from=USD&to=IDR"

response = requests.get(url)
data = response.json()

# Ambil rates
rates = data['rates']

# Convert ke DataFrame
df = pd.DataFrame.from_dict(rates, orient='index')
df.reset_index(inplace=True)

df.columns = ['Date', 'USD_IDR']

# Convert tipe
df['Date'] = pd.to_datetime(df['Date'])

# Simpan
df.to_csv("kurs_history.csv", index=False)

print(df.head())