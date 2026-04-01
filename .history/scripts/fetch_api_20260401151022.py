import requests
import pandas as pd

def get_exchange_rate():
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    data = requests.get(url).json()

    rate = data['rates']['IDR']

    df = pd.DataFrame({
        "date": [data['date']],
        "usd_to_idr": [rate]
    })

    return df

if __name__ == "__main__":
    df = get_exchange_rate()
    df.to_csv("data/raw/kurs.csv", index=False)
    print("Data kurs berhasil diambil!")