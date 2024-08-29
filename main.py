from scripts.data_collection import download_data
from scripts.strategy import moving_average_strategy
from scripts.backtest import backtest_strategy
from scripts.plot import plot_strategy

def main():
    symbol = "BTC-USD"
    start_date = "2020-01-01"
    end_date = "2024-01-01"

    # Data collection
    data = download_data(symbol, start_date, end_date)

    # Strategy implementation
    data = moving_average_strategy(data, short_window=40, long_window=100)

    # Backtesting
    portfolio = backtest_strategy(data)

    # Plotting
    plot_strategy(data, portfolio)

if __name__ == "__main__":
    main()
