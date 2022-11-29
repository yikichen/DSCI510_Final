import cryptocompare
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt

plt.style.use('seaborn-darkgrid')
# Get the API key from the Quantra file located inside the data_modules folder
cryptocompare_API_key = '3f8819922143abe2f04aa3bb17a5be7adc323aa3676690c505c1d8235eedf3c1'
# Set the API key in the cryptocompare object
cryptocompare.cryptocompare._set_api_key_parameter(cryptocompare_API_key)

def get_price_data(ticket):
    '''
    This function takes in a ticker and returns a dataframe with the price data, volume data and market cap data
    in order to do statistical analysis on the data
    we also append the timestamp to the dataframe

    In order to visualize the data, we will use the plotly library

    Args:
        ticket (str): The ticker of the cryptocurrency
    Returns:
        A csv  with the price data, volume data, market cap data and timestamp
        A plotly graph with the price data

    '''
# Fetch the raw price data
    ticker_symbol = ticket
    currency = 'USD'
    limit_value = 2000
    exchange_name = 'CCCAGG'
    data_before_timestamp = datetime(2022, 11, 23, 0, 0)
    raw_price_data = \
        cryptocompare.get_historical_price_hour(
            ticker_symbol,
            currency,
            limit=limit_value,
            exchange=exchange_name,
            toTs=data_before_timestamp
        )

    # Convert the raw price data into a DataFrame
    hourly_price_data = pd.DataFrame.from_dict(raw_price_data)

    # Set the time columns as index and convert it to datetime
    hourly_price_data.set_index("time", inplace=True)
    hourly_price_data['timestamp'] = hourly_price_data.index
    hourly_price_data.index = pd.to_datetime(hourly_price_data.index, unit='s')
    hourly_price_data['datetimes'] = hourly_price_data.index
    hourly_price_data['datetimes'] = hourly_price_data['datetimes'].dt.strftime(
        '%Y-%m-%d')
    
    # write to csv
    hourly_price_data.to_csv(ticket + '_price.csv')

    # Preview the last 5 values of the the first 7 columns of the DataFrame
    hourly_price_data.iloc[:, :6].head()

    # Plot the close price
    plt.figure(figsize=(15, 7))
    plt.plot(hourly_price_data.close)

    # Set title and labels for the plot
    plt.title('BTC Close Price', fontsize=16)
    plt.xlabel('Date', fontsize=15)
    plt.ylabel('Price ($)', fontsize=15)
    plt.tick_params(axis='both', labelsize=15)

    # Show the plot
    plt.show()

if __name__ == '__main__':
    get_price_data('BTC')
    # get_price_data('ETH')
    # get_price_data('SOL')
    # get_price_data('BNB')
    # get_price_data('ADA')