import streamlit as st
import pandas as pd

# =========================
# LOAD DATA
# =========================
df = pd.read_csv("data/processed/final_dataset.csv")
df['Date'] = pd.to_datetime(df['Date'])

df.columns = df.columns.str.strip()

df = df.rename(columns={
    'interest_rate': 'Interest_Rate',
    'value': 'Interest_Rate',
    'FEDFUNDS': 'Interest_Rate'
})

df['Date'] = pd.to_datetime(df['Date'])

# =========================
# TITLE
# =========================
st.title("📊 Currency Prediction Dashboard")

st.write("Dataset pergerakan Gold, Oil, Interest Rate, dan Kurs USD/IDR")

# =========================
# FILTER TANGGAL
# =========================
start_date = st.date_input("Start Date", df['Date'].min())
end_date = st.date_input("End Date", df['Date'].max())

filtered_df = df[(df['Date'] >= pd.to_datetime(start_date)) & 
                 (df['Date'] <= pd.to_datetime(end_date))]

# =========================
# TAMPIL DATA
# =========================
st.subheader("📄 Data Preview")
st.dataframe(filtered_df.head(20))

# =========================
# GRAFIK
# =========================
st.subheader("📈 Grafik Kurs USD/IDR")
st.line_chart(filtered_df.set_index('Date')['USD_IDR'])

st.subheader("🪙 Harga Emas")
st.line_chart(filtered_df.set_index('Date')['Gold'])

st.subheader("🛢️ Harga Oil")
st.line_chart(filtered_df.set_index('Date')['Oil'])

st.subheader("🏦 Interest Rate")
st.line_chart(filtered_df.set_index('Date')['Interest_Rate'])

# =========================
# METRICS
# =========================
st.subheader("📊 Ringkasan")

col1, col2, col3 = st.columns(3)

col1.metric("Rata-rata Kurs", round(filtered_df['USD_IDR'].mean(), 2))
col2.metric("Harga Emas Max", round(filtered_df['Gold'].max(), 2))
col3.metric("Harga Oil Max", round(filtered_df['Oil'].max(), 2))