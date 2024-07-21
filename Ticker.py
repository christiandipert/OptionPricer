import yfinance as yf
import pandas as df
import matplotlib.pyplot as plt

class Ticker:
    
    def __init__(self, symbol):
        self.symbol = yf.Ticker(symbol)
        
    def getInfo(self):
        return self.symbol.info
    
    def getDF(self):
        return yf.download(self.symbol.info['symbol'])
        
    def getDF(self, start, end):
        return yf.download(self.symbol.info['symbol'], start=start, end=end)
        
    def getClose(self, start, end):
        stock = yf.download(self.symbol.info['symbol'], start=start, end=end)
        close = stock.Close.to_frame()
        close.plot()
        
        plt.title(self.symbol.info['symbol'] + " close price from " + start + " - " + end)
        plt.ylabel("Close Price (USD)")
        plt.show()
        