import numpy as np
import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt  # To visualize
from sklearn.linear_model import LinearRegression

def correlation(ticker, subreddit,content,start_date,end_date):
    '''
    This function is to do the correlation analysis between the token price and its sentiment score 
    Correlation is a statistical measure that expresses the extent to which two variables are linearly related.
    Args:
        ticker: the name of the ticker
        subreddit: the name of the subreddit
        content: the content of the post, FTX or all
        start_date: the start date of the post
        end_date: the start date of the post
    Returns:
        correlation result
    ''' 
    df1 = pd.read_csv(ticker + '_'+ 'price.csv',header=0)
    df2 = pd.read_csv(subreddit + '_'+ content + 'trans_sentiment.csv',header=0)
    df1 = df1[df1['timestamp'] >= start_date]
    df1 = df1[df1['timestamp'] <= end_date]
    df2 = df2[df2['time'] >= start_date]
    df2 = df2[df2['time'] <= end_date]
    df2 = df2.rename(columns={'time':'timestamp'})
    df2['timestamp'] = df2['timestamp'] //3600 * 3600
    df2 = df2.groupby('timestamp').mean()
    df_merge = df1.merge(df2, on='timestamp')
    # print(df_merge)



    x = df_merge['close']
    y = df_merge['label']
    z = df_merge['compound']

    print('correlation for ' + ticker + ' and ' + subreddit + ' on ' + content + ' sentiment')
    print('from ' + dt.datetime.fromtimestamp(start_date).strftime('%Y-%m-%d') + ' to ' + dt.datetime.fromtimestamp(end_date).strftime('%Y-%m-%d'))
    print(np.corrcoef(x, y)[0,1])

    #linear regression
    linear_regressor = LinearRegression()  # create object for the class
    x = x.values.reshape(-1, 1)
    y = z.values.reshape(-1, 1)
    linear_regressor.fit(x, y)  # perform linear regression
    Y_pred = linear_regressor.predict(x)  # make predictions
    print('linear regression for ' + ticker + ' and ' + subreddit + ' on ' + content + ' sentiment')
    print('from ' + dt.datetime.fromtimestamp(start_date).strftime('%Y-%m-%d') + ' to ' + dt.datetime.fromtimestamp(end_date).strftime('%Y-%m-%d'))
    print(linear_regressor.coef_)
    plt.scatter(x, y)
    plt.plot(x, Y_pred, color='red')
    plt.show()

    # df_merge.plot(x='close', y='label', style='o')
    # linear_regressor = LinearRegression()
    # linear_regressor.fit(x.values.reshape(-1,1), y.values.reshape(-1,1))
    # Y_pred = linear_regressor.predict(x.values.reshape(-1,1))
    # plt.plot(x, Y_pred, color='red')
    # print(linear_regressor.coef_)

def linear_regression():
    linear_regressor = LinearRegression()  # create object for the class
    return

def correlation_visualization(ticker, subreddit,content,start_date,end_date):

    df1 = pd.read_csv(ticker + '_'+ 'price.csv',header=0)
    df2 = pd.read_csv(subreddit + '_'+ content + 'trans_sentiment.csv',header=0)
    df1 = df1[df1['timestamp'] >= start_date]
    df1 = df1[df1['timestamp'] <= end_date]
    df2 = df2[df2['time'] >= start_date]
    df2 = df2[df2['time'] <= end_date]
    df2 = df2.rename(columns={'time':'timestamp'})
    df2['timestamp'] = df2['timestamp'] //3600 * 3600
    df2 = df2.groupby('timestamp').mean()
    df_merge = df1.merge(df2, on='timestamp')
    df_merge['compound'] = df_merge['compound'] *1000000
    # print(df_merge)
    fig, ax = plt.subplots()
    fig.set_size_inches(14, 8) 
    ax = ax.twinx()
    ax.set_title("BTC Price and Sentiment Score")
    ax.set_xlabel("Time")
    ax.set_ylabel("Price and Sentiment Score")
    price = ax.plot(df_merge['timestamp'],df_merge['close'])
    Score = ax.plot(df_merge['timestamp'],df_merge['compound'])
    all_lines = price + Score
    ax.legend(all_lines, ['Price', 'Sentiment Score'])
    plt.show()

    # df_merge.plot(x = 'timestamp', y = 'close',  label=f"BTC price", alpha=0.5)
    # df_merge.plot( y = 'compound',  label=f"sentiment", alpha=0.5,secondary_y = True)
    # plt.savefig(subreddit +'_'+ content+ '_price_figure.pdf')

def get_visualization(ticker, subreddit,content,start_date,end_date):
    df1 = pd.read_csv(ticker + '_'+ 'price.csv',header=0)
    df2 = pd.read_csv(subreddit + '_'+ content + 'trans_sentiment.csv',header=0)
    df1 = df1[df1['timestamp'] >= start_date]
    df1 = df1[df1['timestamp'] <= end_date]
    df2 = df2[df2['time'] >= start_date]
    df2 = df2[df2['time'] <= end_date]
    df2 = df2.rename(columns={'time':'timestamp'})
    df2['timestamp'] = df2['timestamp'] //3600 * 3600
    df2 = df2.groupby('timestamp').mean()
    df_merge = df1.merge(df2, on='timestamp')
    fig, ax = plt.subplots()
    fig.set_size_inches(14, 8) 
    ax = ax.plot()
    df_merge.plot(x = 'timestamp', y = 'close',  label=f"BTC price", alpha=0.5)
    plt.savefig(subreddit +'_'+ content+ '_price_figure.pdf')
    df_merge.plot( y = 'compound',  label=f"sentiment", alpha=0.5,secondary_y = True)
    plt.savefig(subreddit +'_'+ content+ '_sentiment_figure.pdf')

if __name__ == '__main__':
    start_date = dt.datetime(2022, 11, 11).timestamp()
    end_date = dt.datetime(2022, 11, 19).timestamp()
    # correlation('BTC', 'bitcoin','FTX',start_date,end_date)
    # correlation('BTC', 'cryptocurrency','all',start_date,end_date)
    # correlation_visualization('BTC', 'bitcoin','FTX',start_date,end_date)
    get_visualization('BTC', 'cryptocurrency','all',start_date,end_date)
