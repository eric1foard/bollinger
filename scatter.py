import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def get_data(symbol):
    df = pd.read_csv('./{}.csv'.format(symbol), index_col='Date',parse_dates=True,
                        usecols=['Date', 'Close'], na_values=['nan'])
    df = df.rename(columns={'Close': symbol})
    return df

def compute_daily_returns(df):
    daily_returns = df.copy()
    daily_returns[1:] = (df[1:] / df[:-1].values) - 1
    daily_returns.ix[0, :] = 0 # set daily returns for row 0 to 0
    return daily_returns

def scatter_plot():
    dates = pd.date_range('2016-06-22', '2017-06-22')
    df = pd.DataFrame(index=dates)
    symbols = ['BTC', 'AAPL']

    for symbol in symbols:
        df_temp = get_data(symbol)
        df = df.join(df_temp)

    df = df.dropna()

    daily_returns = compute_daily_returns(df)
    daily_returns.plot(kind='scatter', x='AAPL', y='BTC')
    beta_BTC, alpha_BTC = np.polyfit(daily_returns['AAPL'], daily_returns['BTC'], 1)
    plt.plot(daily_returns['BTC'], beta_BTC*daily_returns['BTC'] + alpha_BTC, '-', color='red')

    # the beta value shows us how the stock moves with respect to the other stock (usually SPY)
    # a higher beta value means that the stock is more reactive to the market

    # the alpha value tell us whether or not a stock outperforms the market (or another stock)
    print 'BETA=',beta_BTC
    print 'alpha=',alpha_BTC
    print 'CC=',daily_returns.corr(method='pearson')
    plt.show()

if __name__ == '__main__':
    scatter_plot()
