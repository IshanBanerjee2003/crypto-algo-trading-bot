# Algorithmic Crypto Trading Bot
This repository contains a cryptocurrency algorithmic trading bot implemented in Python. The bot utilizes a moving average crossover strategy to trade Bitcoin (BTC) against USD. The system is designed to be modular, allowing for easy expansion and customization of trading strategies, data sources, and execution mechanisms.
## Features
- **Data Collection:** Download historical cryptocurrency data from Yahoo Finance.
- **Strategy Implementation:** Moving average crossover strategy to generate buy/sell signals.
- **Backtesting:** Evaluate the strategy's performance using historical data.
- **Visualization:** Plot the trading signals and portfolio performance over time.

## Repository Structure
```bash
crypto-algo-trading-bot/
│
├── README.md
├── data/
│   └── btc_usd_data.csv               # Historical data for BTC-USD
│
├── scripts/
│   ├── data_collection.py             # Script to download and preprocess data
│   ├── strategy.py                    # Script to implement the trading strategy
│   ├── backtest.py                    # Script to backtest the strategy
│   └── plot.py                        # Script to visualize results
│
├── main.py                            # Main script to run the bot
└── requirements.txt                   # Python dependencies
