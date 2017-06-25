import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def get_data(symbol):
    df = pd.read_csv('./{}.csv'.format(symbol), index_col='Date',parse_dates=True,
                        usecols=['Date', 'Close'], na_values=['nan'])
    df = df.rename(columns={'Close': symbol})
    return df

def daily_returns_portfolio(df):
    daily_returns = df.copy()
    daily_returns[1:] = (df[1:] / df[:-1].values) - 1
    daily_returns.ix[0, :] = 0 # set daily returns for row 0 to 0
    return daily_returns

def portfolio_value():
    dates = pd.date_range('2016-06-23', '2017-06-23')
    df = pd.DataFrame(index=dates)
    symbols = ['BTC', 'AAPL']
    # read data into dataframe
    for symbol in symbols:
        df_temp = get_data(symbol)
        df = df.join(df_temp)
    df = df.dropna()

    initial_port_val = 1000
    start_values = df.ix[0].values
    normalized = df / df.ix[0].values # normalize values
    allocated = normalized * [0.5, 0.5] # multiply by allocation
    pos_vals = allocated * initial_port_val # multiply by intial portfolio value
    port_val = pos_vals.sum(axis=1) # get value for each day
    return port_val

def main():
    df = portfolio_value()
    daily_returns = daily_returns_portfolio(pd.DataFrame(df, columns=['Value']))
    print daily_returns
    daily_returns.plot()
    plt.show()

if __name__ == '__main__':
    main()
