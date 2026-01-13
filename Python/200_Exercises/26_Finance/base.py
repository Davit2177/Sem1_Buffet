#Run "pip install yfinance" in a terminal

import yfinance as yf
list = ["YTV.F","LSE","UTF","MSPR","DSEEY","FDX","USD","CTDD","PLSE","QDF"]
lub = input("please choose of the companies: YTV.F,LSE,UTF,MSPR,DSEEY,FDX,USD,CTDD,PLSE,QDF")

for lub in list:
stock = yf.Ticker(lub)
current_price = stock.history(period="1d")["Close"][0]
info = stock.info

print(info["longName"])
print(info["website"])
print("GOOGL Current Price:", current_price)