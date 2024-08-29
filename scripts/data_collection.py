import yfinance as yf

def download_data(symbol, start, end):
    data = yf.download(symbol, start=start, end=end)
    data.to_csv('data/btc_usd_data.csv')
    data['Returns'] = data['Adj Close'].pct_change()
    return data
