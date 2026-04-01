import pandas as pd

__path__

# Load semua data
gold = pd.read_csv("gold.csv")
oil = pd.read_csv("oil.csv")
interest = pd.read_csv("interest_rate.csv")
kurs = pd.read_csv("kurs_history.csv")

# Convert Date
gold['Date'] = pd.to_datetime(gold['Date'])
oil['Date'] = pd.to_datetime(oil['Date'])
interest['Date'] = pd.to_datetime(interest['Date'])
kurs['Date'] = pd.to_datetime(kurs['Date'])

# Ambil kolom penting
gold = gold[['Date', 'Close']].rename(columns={'Close': 'Gold'})
oil = oil[['Date', 'Close']].rename(columns={'Close': 'Oil'})

# Merge semua
df = gold.merge(oil, on='Date', how='inner')
df = df.merge(interest, on='Date', how='inner')
df = df.merge(kurs, on='Date', how='inner')

# Urutkan tanggal
df = df.sort_values('Date')

# Simpan
df.to_csv("final_dataset.csv", index=False)

print(df.head())