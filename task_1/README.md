To access the data, open the data folder and locate the ticker you want the data for. 
The data is organized by columns in csv files. 
One issue encountered was the unnecessary newline that got incorporated from the open() function when processing the tickers. Before processing each ticker, I removed the newline character to take care of this. 
