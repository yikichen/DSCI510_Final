# DSCI510_Final Project
This repository is my DSCI510 Final Project. It contains the following files:
- README.md: This file
- requirements.txt: Python packages required for this project
- get_reddit_data.py: Python script to download data from the web
- get_price_data.py: Python script to download data from the web
- sentiment_analysis.py: Python script to perform sentiment analysis
- T-test.py: Python script to perform t-test
- correlation.py: Python script to perform correlation analysis
- data_visualization.py: Python script to perform data visualization
- bonus_visualization.ipynb: Python script to perform bonus visualization

# Project Description
## Name: Sentiment Analysis on Reddit and its Correlation with Bitcoin Price
In this project, I will compare community attitude on FTX collapse: comparison sentiment analysis on r/Cryptocurrency & r/ Bitcoin Reddit Forum. I will also compare the correlation between Bitcoin price and Reddit sentiment score.
## Background
In November 2022, FTX, one of the world’s largest cryptocurrency companies, announced that it would file for bankruptcy, with its CEO, Sam Bankman-Fried (SBF), stepping down in the wake of a trading scandal that has embroiled the firm in regulatory inquiries. While the media reported it as a fraud and criticized the cryptocurrency industry for its lack of transparency, the blockchain community itself disagreed on whether this was a disgrace for the crypto industry or a good thing, for it demonstrated the value of self-custody and decentralization, which is the opposite of how FTX was operated.

Therefore, this study takes the members of blockchain communities, both in r/Cryptocurrency and r/ Bitcoin Reddit Forum, as objects and studies their attitude toward the collapse of FTX and its CEO SBF, which reveals the ideologies and heterogeneity among the cryptocurrency community. The hypothesis is that the attitude in r/ Bitcoin is more positive than in r/Cryptocurrency because Bitcoin holders are considered more consolidated on the idea of decentralization and have long been looking down on speculative crypto communities. FTX in Using quantitative methods, this study scrapes the headlines on the two forums since November 11th when SBF announced its filing for bankruptcy.

Meanwhile, to understand the relation of community sentiment with the price of cryptocurrency, I will also compare the correlation between Bitcoin price and r/bitcoin Reddit sentiment score.

This study will be helpful for the cryptocurrency industry to understand community sentiment and the correlation between community sentiment and cryptocurrency price. It will contribute to studying the heterogeneity in the cryptocurrency community and the ideology of the cryptocurrency community.

# Dependencies

- Python 3.8.8

# Installation

Install the requirements necessary to run your project:  

```
pip install -r requirements.txt
```

# Running the project

```
python get_reddit_data.py
python get_price_data.py
python sentiment_analysis.py
python T-test.py
python correlation.py
python data_visualization.py
python bonus_visualization.ipynb
```

# Methodology

## Data Collection

There are two sources of data: Reddit and price:
1.	Reddit headlines in 2 months using pushshift.io. Official Reddit API has a limit of 2000 entries, but I fixed it with https://pushshift.io/, which only allows 250 data per request, so I use a loop to get all the data.

2.	Cryptocurrency price data in 2 months using cryptocompare API. https://min-api.cryptocompare.com/

For Reddit data, I’ve collected all headlines from forums r/cryptocurrency (27839), r/bitcoin (6702). r/ethereum, r/solana, and r/binance in the past two months. In total, there are more than 35,000 headline samples.
For Bitcoin, Ethereum, and FTT price data per hour, I collected 2000 samples for each of them in the past two months.

## Sentiment Analysis
1)	I used NLTK Vaper module to analyze the sentiment of Reddit headlines. Vader is a sentiment analysis tool, it can be used to analyze the sentiment of a sentence. However, after plotting the result in a bar chart, I found the model needs to be fixed because more than 50% of headlines are considered neutral.

2)	To fix the problem, I searched online for better NLP models and found transformer hugging-face. With cardiffnlp/twitter-roberta-base-sentiment model, I analyzed the sentiment of headlines again. Fortunately, this model gives much more precise sentiment scores, which I had checked with randomly selected samples. Reference: https://www.kaggle.com/code/robikscube/sentiment-analysis-python-youtube-tutorial/notebook


## Data Analysis
T-test is to compare means
Correlation is to compare the relationship between two variables

After the transformer sentiment analysis, I used the T-test to compare the means of FTX-related headline sentiments in r/cryptocurrency and r/bitcoin. It showed that from 11.11, when FTX announced its bankruptcy, to 11.23, the sentiment of the bitcoin forum is more positive than cryptocurrency forum with statistical significance (P<0.05). 
This finding proves the hypothesis of this study that the Bitcoin community is more positive towards the FTX collapse because the centralized exchange is the opposite of the decentralized promise of Bitcoin.
```
t-test for bitcoin and cryptocurrency on FTX transformer sentiment
from 2022-11-11 to 2022-11-23
t = 2.6550404257292812
p = 0.007979191697112144
```
Then, I use correlation analysis to test if the Bitcoin price is correlated with the FTX sentiment on r/bitcoin. 
```
correlation for BTC and bitcoin on FTX sentiment
from 2022-11-11 to 2022-11-23
0.04042409212680714
```
Results showed Pearson product-moment correlation coefficients R = 0.04, R^2 = 0.0016. The change in BTC sentiment can explain 0.16% of the change in BTC price, which means the two variables have little correlation.


## Data Visualization
1)	I used seaborn to visualize the frequency of sentiment scores of headlines in each forum. Bar chart was used to compare the frequency of sentiment labels in each forum. 

 ![alt text](https://github.com/yikichen/DSCI510_Final/blob/main/visualization/bitcoin_FTX_trans_bar_sentiment.pdf)

 ![alt text](https://github.com/yikichen/DSCI510_Final/blob/main/visualization/cryptocurrency_FTX_trans_bar_sentiment.pdf)

 
 ![alt text](https://github.com/yikichen/DSCI510_Final/blob/main/visualization/bitcoin_sentiment.pdf)
 ![alt text](https://github.com/yikichen/DSCI510_Final/blob/main/visualization/cryptocurrency_sentiment.pdf)


2)	BTC Price interactive: I used plotly to visualize the BTC price in an interactive chart. It is generated as a html and you can easily track the BTC price with the time, which is crucial for my project because the price fluctuates according to many incidents (eg. SBF/ CZ’s twitter thread).

![alt text](https://github.com/yikichen/DSCI510_Final/blob/main/visualization/BTCprice.png)

3)	Btc & crypto sentiment interactive: I used plotly to visualize the r/bitcoin and r/cryptocurrency forum sentiment in an interactive chart. You can easily track the sentiment in comparison on both forum with time. It is generated as a html and you can easily track the BTC price with the time.

![alt text](https://github.com/yikichen/DSCI510_Final/blob/main/visualization/Btccrypto_sentiment.png)

4)	BTC & r/bitcoin sentiment: I used plotly to visualize the BTC price in comparison with r/bitcoin sentiment in an interactive chart. It was a mess at first because the two variables have vast difference in scale. To fix this problem, I added the second y axis so that it looks better in one chart and you can easily trace the change in price with sentiment score.

![alt text](https://github.com/yikichen/DSCI510_Final/blob/main/visualization/BTCr:bitcoin_sentiment.png)

5)	BTC & ETH price, BTC & FTT price: these pairs of variables are also different in scale, so I used the second y-axis as well. In this way, we can see the how the FTX collapse has influenced different tokens in terms of price. Results show that BTC and ETH are highly correlated, while BTC fluctuates more. FTT is less correlated with BTC and has less elasticity.

![alt text](https://github.com/yikichen/DSCI510_Final/blob/main/visualization/btceth_price.png)
![alt text](https://github.com/yikichen/DSCI510_Final/blob/main/visualization/btcftt_price.png)

# Future Work

Given more time, I would like to do the following:
Compare the sentiment of the headlines in different forums
Compare the sentiment of the headlines in different time periods
Compare the reddit sentiment with twitter sentiment.
