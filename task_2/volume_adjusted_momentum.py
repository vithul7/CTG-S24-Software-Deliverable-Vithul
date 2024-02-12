import pandas as pd

volume_adjusted_momentum_data = {}

with open('task_1/tickers.txt', 'r') as file:
    for line in file:
        # removing new line character from symbol
        ticker_symbol = line[0:len(line) - 1]
        ticker_df = pd.read_csv(f'task_1/data/{ticker_symbol}.csv')
        ticker_column = []
        for index, row in ticker_df.iterrows():
            previous_index = index - 15
            # only can calculate with past 15 days data if data is available
            if previous_index >= 0:
                close_fifteen_days_prior = ticker_df.iloc[previous_index, ticker_df.columns.get_loc('Close')]
                close_prev_day = ticker_df.iloc[index-1, ticker_df.columns.get_loc('Close')]
                volume_prev_day = ticker_df.iloc[index-1, ticker_df.columns.get_loc('Volume')]
                price_momentum = (close_prev_day - close_fifteen_days_prior)/(close_fifteen_days_prior)*100/volume_prev_day
                ticker_column.append(price_momentum)
            else:
                ticker_column.append("")
        # full factor data from ticker inserted into dictionary
        volume_adjusted_momentum_data[ticker_symbol] = ticker_column
        
    volume_adjusted_momentum_df = pd.DataFrame(volume_adjusted_momentum_data)
    
    # adding date column as index
    microsoft_df = pd.read_csv(f'task_1/data/MSFT.csv')
    volume_adjusted_momentum_df = volume_adjusted_momentum_df.assign(Date=microsoft_df['Date'])
    volume_adjusted_momentum_df.set_index('Date', inplace=True)
    
    # outputting dataframe to csv
    volume_adjusted_momentum_df.to_csv('task_2/volume_adjusted_momentum_factor.csv')
            
                
      
                

        
