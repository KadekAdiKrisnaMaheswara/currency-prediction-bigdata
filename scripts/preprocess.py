import pandas as pd

# =========================
# EMAS
# =========================
emas = pd.read_csv("data/raw/emas.csv")
emas = emas[['Date', 'Close']]
emas.columns = ['date', 'gold_price']
emas['date'] = pd.to_datetime(emas['date'])

# =========================
# MINYAK
# =========================
minyak = pd.read_csv("data/raw/minyak.csv")
minyak = minyak[['Date', 'Close']]
minyak.columns = ['date', 'oil_price']
minyak['date'] = pd.to_datetime(minyak['date'])

# =========================
# SUKU BUNGA (WORLD BANK)
# =========================
suku = pd.read_csv("data/raw/suku_bunga.csv")

suku = suku[suku['Country Name'] == 'Indonesia']

suku = suku.melt(id_vars=['Country Name'], var_name='year', value_name='interest_rate')
suku = suku.dropna()

suku['date'] = pd.to_datetime(suku['year'])
suku = suku[['date', 'interest_rate']]

# =========================
# RESAMPLE BULANAN
# =========================
emas = emas.set_index('date').resample('M').mean()
minyak = minyak.set_index('date').resample('M').mean()
suku = suku.set_index('date').resample('M').mean()

# =========================
# GABUNG
# =========================
df = emas.join(minyak, how='inner')
df = df.join(suku, how='inner')

# =========================
# SIMPAN
# =========================
df.to_csv("data/processed/final_dataset.csv")

print("AMAN! Dataset siap 🚀")