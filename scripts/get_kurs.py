import requests
import pandas as pd

url = "https://api.exchangerate-api.com/v4/latest/USD"
data = requests.get(url).json()

rates = data['rates']

df = pd.DataFrame(list(rates.items()), columns=['Currency', 'Rate'])

df.to_csv("kurs.csv", index=False)

print("Data kurs berhasil disimpan!")