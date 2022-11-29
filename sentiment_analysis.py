import pandas as pd
from pprint import pprint
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA
from transformers import AutoTokenizer
from transformers import AutoModelForSequenceClassification
from scipy.special import softmax
sia = SIA()
MODEL = f"cardiffnlp/twitter-roberta-base-sentiment"
tokenizer = AutoTokenizer.from_pretrained(MODEL)
model = AutoModelForSequenceClassification.from_pretrained(MODEL)    


def sentiment_analysis(subreddit, content):
    sns.set(style='darkgrid', context='talk', palette='Dark2')
    df = pd.read_csv(subreddit + '_' + content + '_titles.csv',header=0)
    results = []

    for i in range(len(df)):
        pol_score = sia.polarity_scores(df.iloc[i, 0])
        pol_score['headline'] = df.iloc[i, 0]
        pol_score['time'] = df.iloc[i, 1]
        results.append(pol_score)

    pprint(results[:3], width=100)
    print(len(results))
    df = pd.DataFrame.from_records(results)
    df.head()
    df['label'] = 0
    df.loc[df['compound'] > 0, 'label'] = 1
    df.loc[df['compound'] < -0, 'label'] = -1
    df.to_csv( subreddit +'_'+ content +'_sentiment.csv', mode='w', encoding='utf-8', index=False)

def transformer_sentiment_analysis(subreddit, content):
    df = pd.read_csv(subreddit + '_' + content + '_titles.csv',header=0)
    results = []
    # Run for Roberta Model
    for i in range(len(df)):
        encoded_text = tokenizer(df.iloc[i, 0], return_tensors='pt')
        output = model(**encoded_text)
        scores = output[0][0].detach().numpy()
        scores = softmax(scores)
        scores_dict = (df.iloc[i, 0], df.iloc[i, 1], scores[0], scores[1], scores[2])
        #     'roberta_neg' : scores[0],
        #     'roberta_neu' : scores[1],
        #     'roberta_pos' : scores[2]
        # )
        # print(df.iloc[i, 0],scores_dict)
        # pol_score['headline'] = df.iloc[i, 0]
        # pol_score['time'] = df.iloc[i, 1]
        results.append(scores_dict)
    pprint(results[:3], width=100)
    print(len(results))
    df = pd.DataFrame.from_records(results, columns=['headline','time','roberta_neg', 'roberta_neu', 'roberta_pos'])
    df.head()
    df['compound'] = df['roberta_pos'] - df['roberta_neg'] / (1 - df['roberta_neu'])
    df['label'] = 0
    df.loc[df['compound'] > 0, 'label'] = 1
    df.loc[df['compound'] < -0, 'label'] = -1
    df.to_csv( subreddit +'_'+ content +'trans_sentiment.csv', mode='w', encoding='utf-8', index=False)





if __name__ == '__main__':
    content1 = 'FTX'
    content2 = 'all'
    # sentiment_analysis('bitcoin',content1)
    # sentiment_analysis('ethereum',content1)
    # sentiment_analysis('cryptocurrency',content1)
    # sentiment_analysis('solana',content1)
    # sentiment_analysis('binance',content1)

    # sentiment_analysis('bitcoin',content2)
    # sentiment_analysis('ethereum',content2)
    # sentiment_analysis('cryptocurrency',content2)
    # sentiment_analysis('solana',content2)
    # sentiment_analysis('binance',content2)
    # transformer_sentiment_analysis('bitcoin',content1)
    # transformer_sentiment_analysis('ethereum',content1)
    # transformer_sentiment_analysis('cryptocurrency',content1)
    # transformer_sentiment_analysis('solana',content1)
    # transformer_sentiment_analysis('binance',content1)

    transformer_sentiment_analysis('bitcoin',content2)
    # transformer_sentiment_analysis('ethereum',content2)
    transformer_sentiment_analysis('cryptocurrency',content2)


