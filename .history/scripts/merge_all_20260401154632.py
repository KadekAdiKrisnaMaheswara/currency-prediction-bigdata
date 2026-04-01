import pandas as pd

path = "../data/raw/"

# Load semua data
gold = pd.read_csv(path + "gold.csv")
oil = pd.read_csv(path + "oil.csv")
interest = pd.read_csv(path + "interest_rate.csv")
print(interest.columns.tolist())
kurs = pd.read_csv(path + "kurs_history.csv")

# Convert Date
gold['Date'] = pd.to_datetime(gold['Date'])
oil['Date'] = pd.to_datetime(oil['Date'])
interest['Date'] = pd.to_datetime(interest['Date'])
kurs['Date'] = pd.to_datetime(kurs['Date'])

# 🔥 FIX: ubah interest jadi harian
interest = interest.set_index('Date')
interest = interest.resample('D').ffill()
interest = interest.reset_index()

# Ambil kolom penting
gold = gold[['Date', 'Close']].rename(columns={'Close': 'Gold'})
oil = oil[['Date', 'Close']].rename(columns={'Close': 'Oil'})

# Merge semua
df = gold.merge(oil, on='Date', how='inner')
df = df.merge(interest, on='Date', how='left')  # 🔥 ganti left join
df = df.merge(kurs, on='Date', how='inner')

# Urutkan tanggal
df = df.sort_values('Date')

# Simpan
df.to_csv("../data/processed/final_dataset.csv", index=False)

print(df.head())
print(df.isnull().sum())  # cek missing