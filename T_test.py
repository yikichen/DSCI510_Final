import pandas as pd
import scipy.stats as stats
import datetime as dt

def t_test_vader(subreddit1, subreddit2,content, start_date, end_date):
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
    path1 = './data/senti_analysis/nltk_vader/' + subreddit1 + '_' + content + '_sentiment.csv'
    path2 = './data/senti_analysis/nltk_vader/' + subreddit2 + '_' + content + '_sentiment.csv'
    df1 = pd.read_csv(path1,header=0)
    df2 = pd.read_csv(path2,header=0)
    df1 = df1[df1['time'] >= start_date]
    df1 = df1[df1['time'] <= end_date]
    df2 = df2[df2['time'] >= start_date]
    df2 = df2[df2['time'] <= end_date]
    t, p = stats.ttest_ind(df1['label'], df2['label'])
    # t, p = stats.ttest_ind(df1['compound'], df2['compound'])
    print('t-test for ' + subreddit1 + ' and ' + subreddit2 + ' on ' + content + 'nltk vader sentiment')
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
    path1 = './data/senti_analysis/transformer_sentiment/' + subreddit1 + '_' + content + 'trans_sentiment.csv'
    path2 = './data/senti_analysis/transformer_sentiment/' + subreddit2 + '_' + content + 'trans_sentiment.csv'
    df1 = pd.read_csv(path1,header=0)
    df2 = pd.read_csv(path2,header=0)
    df1 = df1[df1['time'] >= start_date]
    df1 = df1[df1['time'] <= end_date]
    df2 = df2[df2['time'] >= start_date]
    df2 = df2[df2['time'] <= end_date]
    # t, p = stats.ttest_ind(df1['label'], df2['label'])
    t, p = stats.ttest_ind(df1['compound'], df2['compound'])
    print('t-test for ' + subreddit1 + ' and ' + subreddit2 + ' on ' + content + 'transformer sentiment')
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
    # t_test_vader('bitcoin', 'ethereum',content1, start_date, end_date)
    # t_test_trans('bitcoin', 'cryptocurrency',content1,start_date,end_date)
    # t_test_vader('bitcoin', 'cryptocurrency',content2,start_date,end_date)

    # t_test_vader('bitcoin', 'solana',content1,start_date,end_date)
    # t_test_vader('bitcoin', 'binance',content1,start_date,end_date)
    # t_test_vader('ethereum', 'cryptocurrency')
    # t_test_vader('ethereum', 'solana')
    # t_test_vader('ethereum', 'binance')
    # t_test_vader('cryptocurrency', 'solana')
    # t_test_vader('cryptocurrency', 'binance')
    # t_test_vader('solana', 'binance')
    t_test_trans('bitcoin', 'cryptocurrency',content1,start_date,end_date)


'''

results:
11-11 to 11-18
bitcoin vs cryptocurrency:
t = 1.9491453502749059
p = 0.05142120031101409

'''