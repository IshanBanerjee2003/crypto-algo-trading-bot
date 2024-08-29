import matplotlib.pyplot as plt

def plot_strategy(data, portfolio):
    fig, ax = plt.subplots(2, figsize=(12,8))

    data['Adj Close'].plot(ax=ax[0], color='r', lw=2.)
    data[['Short_MA', 'Long_MA']].plot(ax=ax[0], lw=2.)
    ax[0].plot(data[data['Position'] == 1.0].index, 
               data['Short_MA'][data['Position'] == 1.0],
               '^', markersize=10, color='m', label='Buy')
    ax[0].plot(data[data['Position'] == -1.0].index, 
               data['Short_MA'][data['Position'] == -1.0],
               'v', markersize=10, color='k', label='Sell')
    ax[0].set_title('Moving Average Trading Strategy')
    ax[0].legend()

    portfolio['Total'].plot(ax=ax[1], lw=2.)
    ax[1].set_title('Portfolio Value')
    plt.show()
