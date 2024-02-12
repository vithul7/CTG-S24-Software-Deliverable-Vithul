# Task: Utilize API to retrieve Date, Open, High, Low, Close, Volume, And Adjusted Close
# Only consider 01/01/2021 to 12/31/2023
# maintain data in CSV files like data/AAPL.csv data/ABBV.csv etc
import yfinance as yf
with open('task_1/tickers.txt', 'r') as file:
    for line in file:
        # removing new line character from symbol
        ticker_symbol = line[0:len(line) - 1]
        start_date = '2021-01-01'
        end_date = '2023-12-31'
        ticker_data = ""
        try:
            ticker_data = yf.download(ticker_symbol, start=start_date, end=end_date)
        except Exception as e:
            print(f"An error occurred fetching the data for {ticker_symbol}")
        
        # converting date to datetime in format seen in sample-factor.csv
        ticker_data.index = ticker_data.index.strftime('%m/%d/%Y')
        
        # saving data to csv file
        ticker_data.to_csv(f'task_1/data/{ticker_symbol}.csv')
