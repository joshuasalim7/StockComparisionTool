import yfinance as yf

def get_stock_info(ticker):
    share_info = yf.Ticker(ticker).info

    # Define the keys of interest
    keys_of_interest = ['currentPrice', 'ebitda', 'freeCashflow', 'trailingEps', 'trailingPE', 'forwardPE']

    # Print stock information
    print(f"\nStock Information for {ticker}:")
    for key in keys_of_interest:
        if key in share_info:
            print(f"{key}: {share_info[key]}")
        else:
            print(f"{key} not available")

# Get stock tickers from the user
num_stocks = int(input("Enter the number of stocks to compare: "))
tickers = [input(f"Enter share name {i+1}: ") for i in range(num_stocks)]

# Get and print the information for each stock
for ticker in tickers:
    get_stock_info(ticker)
