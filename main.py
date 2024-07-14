import numpy as np
import matplotlib.pyplot as plt
import sklearn as sk
from Ticker import *
import yfinance as yf

def main():
    ticker = Ticker('MSFT')
    info = ticker.getInfo() # LARGE Json
    ticker.plotClose(start="2020-07-14", end="2024-07-14") # Example of plotClose()

if __name__ == "__main__":
    main()
    