import pandas as pd
import scipy.stats as stats
import datetime as dt

def t_test(subreddit1, subreddit2,content, start_date, end_date):
    '''
    This function is to do the t-test
    T-test is to compare the means of two groups to determine whether there is statistical significance between the two groups
    Args:
        subreddit1: the name of the first subreddit
        subreddit2: the name of the second subreddit
        content: the content of the post, FTX or ALL
        start_date: the start date of the post
        end_date: the end date of the post
    Returns:
        t-test result
    
    '''
    df1 = pd.read_csv(subreddit1 + '_'+ content + '_sentiment.csv',header=0)
    df2 = pd.read_csv(subreddit2 + '_'+ content + '_sentiment.csv',header=0)
    df1 = df1[df1['time'] >= start_date]
    df1 = df1[df1['time'] <= end_date]
    df2 = df2[df2['time'] >= start_date]
    df2 = df2[df2['time'] <= end_date]
    t, p = stats.ttest_ind(df1['label'], df2['label'])
    # t, p = stats.ttest_ind(df1['compound'], df2['compound'])
    print('t-test for ' + subreddit1 + ' and ' + subreddit2 + ' on ' + content + ' sentiment')
    print('from ' + dt.datetime.fromtimestamp(start_date).strftime('%Y-%m-%d') + ' to ' + dt.datetime.fromtimestamp(end_date).strftime('%Y-%m-%d'))
    print('t = ' + str(t))
    print('p = ' + str(p))
    print('')
    return


def t_test_trans(subreddit1, subreddit2,content, start_date, end_date):
    '''
    This function is to do the t-test
    T-test is to compare the means of two groups to determine whether there is statistical significance between the two groups
    Args:
        subreddit1: the name of the first subreddit
        subreddit2: the name of the second subreddit
        content: the content of the post, FTX or ALL
        start_date: the start date of the post
        end_date: the end date of the post
    Returns:
        t-test result
    
    '''
    df1 = pd.read_csv(subreddit1 + '_'+ content + 'trans_sentiment.csv',header=0)
    df2 = pd.read_csv(subreddit2 + '_'+ content + 'trans_sentiment.csv',header=0)
    df1 = df1[df1['time'] >= start_date]
    df1 = df1[df1['time'] <= end_date]
    df2 = df2[df2['time'] >= start_date]
    df2 = df2[df2['time'] <= end_date]
    # t, p = stats.ttest_ind(df1['label'], df2['label'])
    t, p = stats.ttest_ind(df1['compound'], df2['compound'])
    print('t-test for ' + subreddit1 + ' and ' + subreddit2 + ' on ' + content + ' sentiment')
    print('from ' + dt.datetime.fromtimestamp(start_date).strftime('%Y-%m-%d') + ' to ' + dt.datetime.fromtimestamp(end_date).strftime('%Y-%m-%d'))
    print('t = ' + str(t))
    print('p = ' + str(p))
    print('')
    return

if __name__ == '__main__':
    content1 = 'FTX'
    content2 = 'all'
    start_date = dt.datetime(2022, 11, 11).timestamp()
    end_date = dt.datetime(2022, 11, 23).timestamp()
    # t_test('bitcoin', 'ethereum',content1, start_date, end_date)
    t_test_trans('bitcoin', 'cryptocurrency',content1,start_date,end_date)
    # t_test('bitcoin', 'cryptocurrency',content2,start_date,end_date)

    # t_test('bitcoin', 'solana',content1,start_date,end_date)
    # t_test('bitcoin', 'binance',content1,start_date,end_date)
    # t_test('ethereum', 'cryptocurrency')
    # t_test('ethereum', 'solana')
    # t_test('ethereum', 'binance')
    # t_test('cryptocurrency', 'solana')
    # t_test('cryptocurrency', 'binance')
    # t_test('solana', 'binance')
    t_test('bitcoin', 'cryptocurrency',content2,start_date,end_date)


'''

results:
11-11 to 11-18
bitcoin vs cryptocurrency:
t = 1.9491453502749059
p = 0.05142120031101409

'''