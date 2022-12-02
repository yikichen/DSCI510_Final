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
- bonus_visualization.py: Python script to perform bonus visualization

# Project Description
## Title: Sentiment Analysis on Reddit and its Correlation with Bitcoin Price
In this project, I will compare community attitude on FTX collapse: comparison sentiment analysis on r/Cryptocurrency & r/ Bitcoin Reddit Forum. I will also compare the correlation between Bitcoin price and Reddit sentiment score.
## Background
In November 2022, FTX, one of the world’s largest cryptocurrency companies, announced that it would file for bankruptcy, with its CEO, Sam Bankman-Fried (SBF), stepping down in the wake of a trading scandal that has embroiled the firm in regulatory inquiries. While the media reported it as a fraud and criticized the cryptocurrency industry for its lack of transparency, the blockchain community itself disagreed on whether this was a disgrace for the crypto industry or a good thing, for it demonstrated the value of self-custody and decentralization, which is the opposite of how FTX was operated.

Therefore, this study takes the members of blockchain communities, both in r/Cryptocurrency and r/ Bitcoin Reddit Forum, as objects and studies their attitude toward the collapse of FTX and its CEO SBF, which reveals the ideologies and heterogeneity among the cryptocurrency community. The hypothesis is that the attitude in r/ Bitcoin is more positive than in r/Cryptocurrency because Bitcoin holders are considered more consolidated on the idea of decentralization and have long been looking down on speculative crypto communities. FTX in Using quantitative methods, this study scrapes the headlines on the two forums since November 11th when SBF announced its filing for bankruptcy.

Meanwhile, in order to understand the relation of community sentiment with the price of cryptocurrency, I will also compare the correlation between Bitcoin price and r/bitcoin Reddit sentiment score.

This study will be helpful for the cryptocurrency industry to understand the community sentiment and the correlation between community sentiment and cryptocurrency price. It will also be helpful for the cryptocurrency industry to understand the heterogeneity among the cryptocurrency community. Especially, this study will contribute to the research on the ideology and history of the cryptocurrency community.

# Dependencies

- Python 3.8.8

# Installation

Install the requirements necessary to run your project:  

```
pip install -r requirements.txt
```

# Running the project

Typically, a single file is called to run the project (something along the lines of)  

```
python get_reddit_data.py
python get_price_data.py
python sentiment_analysis.py
python T-test.py
python correlation.py
python data_visualization.py
python bonus_visualization.py
```

# Methodology

## Data Collection
reddit API only allows 2000 data per request, so I use the https://api.pushshift.io
https://api.pushshift.io only allows 250 data per request, so I use loop to get all the data


## Sentiment Analysis
1)	I used NLTK Vaper module to analyze the sentiment of Reddit headlines. However, after plotting the result in a bar chart, I found the model needs to be fixed because more than 50% of headlines are considered neutral.

Vader is a sentiment analysis tool, it can be used to analyze the sentiment of a sentence
However, it is not very accurate, so I use the sentiment analysis tool of Transformers
Reference: https://www.kaggle.com/code/robikscube/sentiment-analysis-python-youtube-tutorial/notebook

2)	To fix the problem, I searched online for better NLP models and found transformer hugging-face. With cardiffnlp/twitter-roberta-base-sentiment model, I analyzed the sentiment of headlines again. Fortunately, this model gives much more precise sentiment scores, which I had checked with randomly selected samples.

## Data Analysis
T-test is to compare means
Correlation is to compare the relationship between two variables

After the transformer sentiment analysis, I used the T-test to compare the means of FTX-related headline sentiments in r/cryptocurrency and r/bitcoin. It showed that from 11.11, when FTX announced its bankruptcy, to 11.23, the sentiment of the bitcoin forum is more positive than cryptocurrency forum with statistic significance (P<0.05).
t-test for bitcoin and cryptocurrency on FTX transformer sentiment
from 2022-11-11 to 2022-11-23
t = 2.6550404257292812
p = 0.007979191697112144
Then, I use correlation analysis to test if the Bitcoin price is correlated with the FTX sentiment on r/bitcoin. Result show that 
correlation for BTC and bitcoin on FTX sentiment
from 2022-11-11 to 2022-11-23
0.04042409212680714

Results showed that Pearson product-moment correlation coefficients R = 0.04, R^2 = 0.0016, which means that the change in BTC sentiment can explain 0.16% of the change in BTC price, which means the two variables have little correlation with the other.


## Data Visualization
I used seaborn to visualize the frequency of sentiment scores of headlines in each forum. Bar chart was used to compare the frequency of sentiment labels in each forum. 

I used plotly to visualize the BTC price in an interactive chart. It is generated as a html and you can easily track the BTC price with the time, which is crucial for my project because the price fluctuated according to many incidents (eg. SBF/ CZ’s twitter thread).

I used plotly to visualize the BTC and crypto forum sentiment in an interactive chart. It is generated as a html and you can easily track the BTC price with the time, which is crucial for my project because the price fluctuated according to many incidents (eg. SBF/ CZ’s twitter thread).


# Future Work

Given more time, I would like to do the following:
Compare the sentiment of the headlines in different forums
Compare the sentiment of the headlines in different time periods
