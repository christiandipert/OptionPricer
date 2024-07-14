import numpy as np
import matplotlib as plt
import Ticker

class BlackScholes:
    
    # BS VARIABLES
    # S = price of stock
    # V(S, t) = price(S, time)
    # C(S, t) = price(S, t) of european Call Option
    # P(S, t) = price(S, t) of european Put Option
    # K = strike price
    # r = annualized risk-free interest rate, compounded continuously
    # mu = drift rate of S annualized
    # sigma = std dev of stock (sqrt of quadratic variation of log price)
    # t = time in years. now=0, expiry=T
    
    # OTHER
    # pi = value of the portfolio
    # R = accumulated profit of delta-hedging strategy
    # N(x) = cdf = integral(-inf, x) pdf dz = (1/sqrt(2pi)) * integral(-inf, x)(e^(x^2 / 2))dz
    # N'(x) = pdf = e^(-x^2 / 2)/2pi

    def __init__(self, Ticker):
        self.ticker = Ticker
        
    def callOption():
        
        # B.S. Call Option Price (Holy Grail):
        # 
        # C(S,t) = N(d1)S - N(d2)Ke^(-r(T-t))
        # 
        # where:
        # d1 = (ln(S/K) + (r + (sigma^2)/2)(T-t)) / (sigma * sqrt(T-t)),
        # d2 = d1 - sigma * sqrt(T-t)
        # 
        # where:
        # T - t = days to expiration = time to maturity
        # S = curr spot price of underlying asset
        # K = strike price
        # r = risk free rate (annual) (continuous compound)
        # sigma = std dev (volatility)
        
        return 0
    
    def putOption():
        
        # B.S. PUT Option Price (Holy Grail):
        # (put-call parity invoked)
        # P(S,t) = Ke^(-r(T-t)) - S + C(S,t)
        #        = (1-N(d2))Ke^(-r(T-t)) - (1-N(d1)) * S
        # 
        # where:
        # d1 = (ln(S/K) + (r + (sigma^2)/2)(T-t)) / (sigma * sqrt(T-t)),
        # d2 = d1 - sigma * sqrt(T-t)
        # 
        # where:
        # T - t = days to expiration = time to maturity
        # S = curr spot price of underlying asset
        # K = strike price
        # r = risk free rate (annual) (continuous compound)
        # sigma = std dev (volatility)
        
        return 0
    
    # Calculate average return over k months
    def avgReturn(ticker, k):
        return 0
    
    # STD Deviation of return
    def sigma(histReturns, avgReturn, months):
        # use prices = np.array(time, price), then std_dev = np.std(prices)
        sigma = 0.0
        return sigma