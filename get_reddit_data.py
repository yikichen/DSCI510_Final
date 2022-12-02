import json
import requests
import pandas as pd
import requests
import json
import datetime as dt

'''
This script is to get the headlines from reddit
customize the subreddit name, start date and end date
then run the script

git repo:
https://github.com/yikichen/DSCI510_Final
'''


def get_249_title(url,subreddit,created_time):
    '''
    This function is to get the 250 titles of the post
    Args:
        url: the url of the post
        subreddit: the subreddit name
        created_time: the time when the post is created
    Returns:
        data: append data to csv file with the title of the post
    '''

    try:
        response = requests.request("GET", url)
        dict_re = response.text
        re_json = json.loads(dict_re)
        ftx_results = []
        title_ls = set()
        for i in re_json['data']:
            title_ls.add((i['title'],i['created_utc']))
            created_time.append(i['created_utc'])
        for index, tuple in enumerate(title_ls):
            line = tuple[0]
            if 'ftx' in line or'FTX' in line or 'sbf' in line or 'SBF' in line or 'Sam' in line:
                ftx_results.append(tuple)
        df1 = pd.DataFrame(title_ls).dropna()
        df2 = pd.DataFrame(ftx_results).dropna()
        path1 = str('./data/reddit_data') + '/' + str(subreddit) + '_all_titles.csv'
        path2 = str('./data/reddit_data') + '/' + str(subreddit) + '_FTX_titles.csv'
        df1.to_csv(path1, mode='a', encoding='utf-8', index=False)
        df2.to_csv(path2, mode='a', encoding='utf-8', index=False)
    except:
        pass
    return 


def renew_url_with_time(time,subreddit):
    '''
    This function is to renew the url with the time
    Because the reddit api only allows to get 250 posts at a time
    So we need to renew the url with the time of the last post

    Args:
        time: the time when the post is created
        subreddit: the subreddit name
    Returns:
        url: the url of the post
    '''
    new_url = "https://api.pushshift.io/reddit/submission/search/?after=" + str(time) + "&subreddit=" + subreddit + "&size=249"
    return new_url

def get_data(created_time,subreddit,end_date):
    '''
    This function is to get ALL the data from reddit, loop over the function get_249_title
    Args:
        created_time: the time when the post is created
        subreddit: the subreddit name
        end_date: the end date of the data
    Returns:
        data: a complete csv file with the title of the post
    '''
    while int(created_time[-1]) < int(end_date):
        get_249_title(renew_url_with_time(created_time[-1],subreddit),subreddit,created_time)
        print(created_time[-1])
    path1 = str('./data/reddit_data') + '/' + str(subreddit) + '_FTX_titles.csv'
    path2 = str('./data/reddit_data') + '/' + str(subreddit) + '_all_titles.csv'
    df1 = pd.read_csv(subreddit+'_FTX_titles.csv',header=None, names=['Headlines','Time'])
    df1 = df1[df1['Headlines'] != '0'].dropna()
    df1.to_csv(path1, mode='w', encoding='utf-8', index=False)
    df2 = pd.read_csv(subreddit+'_all_titles.csv',header=None, names=['Headlines','Time'])
    df2 = df2[df2['Headlines'] != '0'].dropna()
    df2.to_csv(path2, mode='w', encoding='utf-8', index=False)
    return 


if __name__ == '__main__':
    '''
    created_time_bitcoin = ['1668146400'] #the time epoch of Nov 11 2022
    '''
    created_time_1 = [int(dt.datetime(2022, 10, 10).timestamp())]
    subreddit_1 = 'bitcoin'
    end_date_1 = dt.datetime(2022, 11, 23).timestamp()
    get_data(created_time_1,subreddit_1,end_date_1)

    created_time_2 = [int(dt.datetime(2022, 10, 10).timestamp())]
    subreddit_2 = 'cryptocurrency'
    end_date_2 = dt.datetime(2022, 11, 23).timestamp()
    get_data(created_time_2,subreddit_2,end_date_2)

    created_time_3 = [int(dt.datetime(2022, 10, 10).timestamp())]
    subreddit_3 = 'ethereum'
    end_date_3 = dt.datetime(2022, 11, 23).timestamp()
    get_data(created_time_3,subreddit_3,end_date_3)
    
    created_time_4 = [int(dt.datetime(2022, 10, 10).timestamp())]
    subreddit_4 = 'solana'
    end_date_4 = dt.datetime(2022, 11, 23).timestamp()
    get_data(created_time_4,subreddit_4,end_date_4)

    created_time_5 = [int(dt.datetime(2022, 10, 10).timestamp())]
    subreddit_5 = 'binance'
    end_date_5 = dt.datetime(2022, 11, 23).timestamp()
    get_data(created_time_5,subreddit_5,end_date_5)