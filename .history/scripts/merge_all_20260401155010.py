import pandas as pd

path = "../data/raw/"

# =========================
# LOAD DATA
# =========================
gold = pd.read_csv(path + "gold.csv")
oil = pd.read_csv(path + "oil.csv")
interest = pd.read_csv(path + "interest_rate.csv, sep")
kurs = pd.read_csv(path + "kurs_history.csv")

# =========================
# BERSIHKAN NAMA KOLOM
# =========================
gold.columns = gold.columns.str.strip()
oil.columns = oil.columns.str.strip()
interest.columns = interest.columns.str.strip().str.lower()
kurs.columns = kurs.columns.str.strip()

print("Interest columns:", interest.columns.tolist())

# =========================
# RENAME KOLOM (PAKSA AMAN)
# =========================
interest = interest.rename(columns={
    'date': 'Date',
    'fedfunds': 'Interest_Rate',
    'value': 'Interest_Rate'
})

# =========================
# CONVERT DATE
# =========================
gold['Date'] = pd.to_datetime(gold['Date'], errors='coerce')
oil['Date'] = pd.to_datetime(oil['Date'], errors='coerce')
interest['Date'] = pd.to_datetime(interest['Date'], errors='coerce')
kurs['Date'] = pd.to_datetime(kurs['Date'], errors='coerce')

# =========================
# HANDLE INTEREST (BULANAN → HARIAN)
# =========================
interest = interest.set_index('Date')
interest = interest.resample('D').ffill()
interest = interest.reset_index()

# =========================
# PILIH KOLOM PENTING
# =========================
gold = gold[['Date', 'Close']].rename(columns={'Close': 'Gold'})
oil = oil[['Date', 'Close']].rename(columns={'Close': 'Oil'})

# =========================
# MERGE
# =========================
df = gold.merge(oil, on='Date', how='inner')
df = df.merge(interest, on='Date', how='left')
df = df.merge(kurs, on='Date', how='inner')

# =========================
# FINAL TOUCH
# =========================
df = df.sort_values('Date')

# CEK DATA KOSONG
print("\nMissing values:\n", df.isnull().sum())

# SIMPAN
df.to_csv("../data/processed/final_dataset.csv", index=False)

print("\nData berhasil digabung!")
print(df.head())