import numpy as np
import matplotlib.pyplot as plt
import sklearn as sk
from Ticker import *
from BlackScholes import BlackScholes
import pprint
import yfinance as yf

def main():
    ticker = Ticker('GME')
    info = ticker.getInfo() # LARGE Json
    blackScholes = BlackScholes(ticker)
    print(blackScholes.sigma(ticker, "2020-07-14", "2024-07-14"))
    # ticker.plotClose(start="2020-07-14", end="2024-07-14") # Example of plotClose()

if __name__ == "__main__":
    main()
    