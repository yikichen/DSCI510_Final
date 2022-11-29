import pandas as pd
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style='darkgrid', context='talk', palette='Dark2')

def visualize_sentiment(subreddit,content):
    '''
    This function is to visualize the sentiment of the post
    Args:
        subreddit: the subreddit name
        content: the content of the post
    Returns:
        A plotly graph with the sentiment of the post
    '''
    df = pd.read_csv(subreddit +'_' + content + '_sentiment.csv',header=0)
    df.label.value_counts(normalize=True) * 100
    fig, ax = plt.subplots(figsize=(8, 8))
    counts = df.label.value_counts(normalize=True) * 100

    sns.barplot(x=counts.index, y=counts, ax=ax)
    ax.set_title(subreddit.capitalize() + ' Sentiment')
    ax.set_xticklabels(['Negative', 'Neutral', 'Positive'])
    ax.set_ylabel("Percentage")
    plt.savefig(subreddit + '_sentiment.pdf')

    # plt.style.use('ggplot')
    # fig, axs = plt.subplots(1, 3, figsize=(12, 3))
    # sns.barplot(data= df, x=counts.index, y=counts, ax=axs[0])
    # sns.barplot(data= df, x=counts.index, y=counts, ax=axs[1])
    # sns.barplot(data= df, x=counts.index, y=counts,  ax=axs[2])
    # axs[0].set_title('Positive')
    # axs[1].set_title('Neutral')
    # axs[2].set_title('Negative')
    # plt.tight_layout()
    # plt.show()


    # ax = sns.barplot(x=counts.index, y=counts, ax=ax)
    # ax.set_title('Compund Score')
    # plt.show()
    # fig, ax1 = plt.subplots(nrows=1, ncols=2, figsize=(9, 4))

def visualize_sentiment_trans(subreddit,content):
    '''
    This function is to visualize the sentiment of the post
    Args:
        subreddit: the subreddit name
        content: the content of the post
    Returns:
        A plotly graph with the sentiment of the post
    '''
    df = pd.read_csv(subreddit +'_' + content + 'trans_sentiment.csv',header=0)
    df.label.value_counts(normalize=True) * 100
    fig, ax = plt.subplots(figsize=(8, 8))
    counts = df.label.value_counts(normalize=True) * 100

    
    
    fig, ax = plt.subplots(1, 1, figsize=(20, 10))
    ax.hist(df['compound'], bins=100, label=f"sentiment frequency", alpha=0.5)
    ax.legend()

    # sns.barplot(x=counts.index, y=counts, ax=ax)
    ax.set_title(subreddit.capitalize() + content +' Reddit Headlines Sentiment Analysis', fontsize=20, fontweight='bold', pad=20)
    # ax.set_xticklabels(['Negative', 'Positive'])
    # ax.set_ylabel("Percentage")
    plt.savefig(subreddit +'_'+ content+ '_trans_sentiment.pdf')

if __name__ == '__main__':
    content1 = 'FTX'
    content2 = 'all'
    visualize_sentiment_trans('bitcoin',content1)
    # visualize_sentiment('ethereum',content1)
    visualize_sentiment_trans('cryptocurrency',content1)
    # visualize_sentiment('solana',content1)
    # visualize_sentiment('binance',content1)
    visualize_sentiment_trans('bitcoin',content2)

    visualize_sentiment_trans('cryptocurrency',content2)
