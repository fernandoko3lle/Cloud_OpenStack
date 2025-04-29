import yfinance as yf
from datetime import datetime, timedelta

def get_bovespa_data():
    hoje = datetime.now()
    inicio = hoje - timedelta(days=14)
    ticker = "^BVSP"

    df = yf.download(ticker, start=inicio.strftime("%Y-%m-%d"), end=hoje.strftime("%Y-%m-%d"))
    df = df.tail(10).reset_index()
    df["Date"] = df["Date"].dt.strftime("%Y-%m-%d")

    resultado = []
    for _, row in df.iterrows():
        resultado.append({
            "Date": row["Date"],
            "Open": row["Open"],
            "High": row["High"],
            "Low": row["Low"],
            "Close": row["Close"],
            "Volume": int(row["Volume"]),
        })

    return resultado