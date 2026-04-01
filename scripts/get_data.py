import yfinance as yf
import pandas as pd

# Ambil data GOLD
gold = yf.download("GC=F", start="2021-01-01", end="2026-01-01")

# Ambil data OIL
oil = yf.download("CL=F", start="2021-01-01", end="2026-01-01")

# Reset index supaya ada kolom Date
gold.reset_index(inplace=True)
oil.reset_index(inplace=True)

# Simpan ke CSV
gold.to_csv("gold.csv", index=False)
oil.to_csv("oil.csv", index=False)

print("Data berhasil disimpan!")