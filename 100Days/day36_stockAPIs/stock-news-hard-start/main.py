import requests
from datetime import date, timedelta

"""Get the previous few days' datetime"""
today = date.today().strftime('%Y-%m-%d')
yesterday = (date.today() - timedelta(days=1)).strftime('%Y-%m-%d')
day_before = (date.today() - timedelta(days=2)).strftime('%Y-%m-%d')

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": "TSLA",
    "interval": "60min",    
    "apikey": "0I9TRC6RIK0LK6US",
    }

## STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. 
# e.g. 40 - 20 = -20, but the positive difference is 20.
#HINT 2: Work out the value of 5% of yerstday's closing stock price. 

response = requests.get(STOCK_ENDPOINT, params=stock_params)
response.raise_for_status()
data = response.json()
yesterday_end_price = float(data["Time Series (Daily)"][str(yesterday)]["4. close"])
print(f"Yesterday's closing price: {yesterday_end_price}")
day_before_end_price = float(data["Time Series (Daily)"][str(day_before)]["4. close"])
print(f"The day before's closing price: {day_before_end_price}")

price_change = yesterday_end_price - day_before_end_price
price_change = abs(price_change)    # abs changes the number to an absolute value (no '-')
print(f"Difference: {round(price_change, 3)}")
percent_change = (price_change / yesterday_end_price) * 100
print(f"Percentage change: {round(percent_change, 3)}%")      # format the number down to fewer decimal points...
if percent_change >= 5:
    print("Get news!")
else:
    print("Minor fluctuations...")

# print(data)

## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME. 
#HINT 1: Think about using the Python Slice Operator



## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number. 
#HINT 1: Consider using a List Comprehension.



#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

