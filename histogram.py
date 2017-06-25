import pandas as pd
import matplotlib.pyplot as plt

# read in CSV from file
def get_stock_data():
    prices = pd.read_csv('./bitstampusd.csv', index_col='Date',parse_dates=True,
                        usecols=['Date', 'Close'], na_values=['nan'])
    dates = pd.date_range('2016-06-22', '2017-06-22')
    df = pd.DataFrame(index=dates)
    df = df.join(prices)
    df = df.dropna()
    return df

def compute_daily_returns(df):
    daily_returns = df.copy()
    daily_returns[1:] = (df[1:] / df[:-1].values) - 1
    daily_returns.ix[0, :] = 0 # set daily returns for row 0 to 0
    return daily_returns

def plot_stock_data(df):
    ax = df['Close'].plot(title='Bitcoin', label='BTC')
    plt.show()

def histogram():
    df = get_stock_data()
    daily_returns = compute_daily_returns(df)
    daily_returns.hist(bins=100, edgecolor='black')
    plt.axvline(daily_returns['Close'].mean(), color='w', linestyle='dashed',linewidth=2)
    std = daily_returns['Close'].std()
    plt.axvline(std, color='r', linestyle='dashed',linewidth=2)
    plt.axvline(-std, color='r', linestyle='dashed',linewidth=2)
    plt.axvline(2*std, color='r', linestyle='dashed',linewidth=2)
    plt.axvline(2*-std, color='r', linestyle='dashed',linewidth=2)
    plt.axvline(3*std, color='r', linestyle='dashed',linewidth=2)
    plt.axvline(3*-std, color='r', linestyle='dashed',linewidth=2)
    print 'kurtosis=',daily_returns.kurtosis()
    plt.show()

if __name__ == '__main__':
    histogram()
