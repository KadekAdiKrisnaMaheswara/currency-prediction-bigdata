import requests
import pandas as pd

url = "https://api.exchangerate.host/timeseries"
params = {
    "start_date": "2021-01-01",
    "end_date": "2026-01-01",
    "base": "USD",
    "symbols": "IDR"
}

response = requests.get(url, params=params)
data = response.json()

rates = data['rates']

# Ubah ke DataFrame
df = pd.DataFrame.from_dict(rates, orient='index')
df.reset_index(inplace=True)

df.columns = ['Date', 'USD_IDR']

df['Date'] = pd.to_datetime(df['Date'])

df.to_csv("kurs_history.csv", index=False)

print("Kurs historis berhasil disimpan!")