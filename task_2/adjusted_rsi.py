import pandas as pd

adjusted_rsi_data = {}

with open('task_1/tickers.txt', 'r') as file:
    for line in file:
        # removing new line character from symbol
        ticker_symbol = line[0:len(line) - 1]
        ticker_df = pd.read_csv(f'task_1/data/{ticker_symbol}.csv')
        ticker_column = []

        for index, row in ticker_df.iterrows():
            previous_index = index - 15
            # only can calculate with past days data if data is available
            if previous_index >= 0:
                # past 15 adjusted closes
                adjusted_close_data = ticker_df.iloc[previous_index: index]
                delta = adjusted_close_data['Adj Close'].diff()
                gain = 0
                loss = 0
                for item in delta:
                    if item > 0:
                        gain += item
                    elif item < 0:
                        loss -= item
                rs = gain / loss
                rsi = 100 - (100 / (1 + rs))
                ticker_column.append(rsi)
            else:
                ticker_column.append("")
        # full factor data from ticker inserted into dictionary
        adjusted_rsi_data[ticker_symbol] = ticker_column
        
    adjusted_rsi_df = pd.DataFrame(adjusted_rsi_data)
    
    # adding date column as index
    microsoft_df = pd.read_csv(f'task_1/data/MSFT.csv')
    adjusted_rsi_df = adjusted_rsi_df.assign(Date=microsoft_df['Date'])
    adjusted_rsi_df.set_index('Date', inplace=True)
    
    # outputting dataframe to csv
    adjusted_rsi_df.to_csv('task_2/adjusted_rsi_factor.csv')
            
                
      
                

        
