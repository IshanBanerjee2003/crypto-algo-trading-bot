import pandas as pd

def backtest_strategy(data):
    initial_capital = 10000.0
    positions = pd.DataFrame(index=data.index).fillna(0.0)
    positions['Asset'] = data['Signal'] * (initial_capital / data['Adj Close'][0])
    portfolio = positions.multiply(data['Adj Close'], axis=0)
    pos_diff = positions.diff()

    portfolio['Holdings'] = (positions.multiply(data['Adj Close'], axis=0)).sum(axis=1)
    portfolio['Cash'] = initial_capital - (pos_diff.multiply(data['Adj Close'], axis=0)).sum(axis=1).cumsum()
    portfolio['Total'] = portfolio['Cash'] + portfolio['Holdings']
    portfolio['Returns'] = portfolio['Total'].pct_change()
    return portfolio
