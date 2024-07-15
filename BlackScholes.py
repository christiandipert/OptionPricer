import numpy as np
import requests
import matplotlib as plt
import scipy.stats as stats
from datetime import datetime
from API_KEYS import AV_API_KEY
import Ticker
import math

# ASSUMPTIONS:
# • It is possible to borrow and lend cash at a known constant risk-free interest rate.
# • The stock price follows a geometric Brownian motion with constant drift and volatility.
# • There are no transaction costs, taxes or bid-ask spread.
# • The underlying security does not pay a dividend.[4]
# • All securities are infinitely divisible (i.e., it is possible to buy any fraction of a share).
# • There are no restrictions on short selling.
# • There is no arbitrage opportunity.

class BlackScholes:
    
    INFL_RATE = 2.97 # percent
    
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
        self.r = self.riskFreeRate()
        
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
        # d1 & d2 = Probability of option expiring ITM (exp-martingale prob measure)
        #         = (ln(S/K) + (r + (sigma^2)/2)(T-t)) / (sigma * sqrt(T-t)),
        # 
        # also,d2 = d1 - sigma * sqrt(T-t)
        # 
        # where:
        # T - t = days to expiration = time to maturity
        # S = curr spot price of underlying asset
        # K = strike price
        # r = risk free rate (annual) (continuous compound)
        # sigma = std dev (volatility)
        
        return 0
    
    # r
    # uses alphavantage API to return most recent nominal risk-free rate
    def riskFreeRate(self):
        url = f'https://www.alphavantage.co/query?function=TREASURY_YIELD&interval=monthly&maturity=10year&apikey={AV_API_KEY}'
        r = requests.get(url)
        data = r.json()
        return float(data['data'][0]['value'])
    
    # S
    def getUnderlyingPrice(self):
        return self.ticker.getInfo()['currentPrice']
        
    # Calculate average return over k months
    def avgReturn(ticker, k):
        return 0
    
    # STD Deviation of return
    def sigma(histReturns, avgReturn, months):
        # use prices = np.array(time, price), then std_dev = np.std(prices)
        sigma = 0.0
        return sigma
    
    # CDF of normal dist func
    def N(T, t, sigma, S, K, r):
        d1 = (1 / (sigma * (T - t) ** 0.5)) * (math.log(S / K) + (r + 0.5 * sigma ** 2) * (T - t))
        return stats.norm.cdf(d1)
    
    def greeks(greek, call, sigma, r, K, S, T, t, d1):
        # change in call price over price of security
        if greek == "delta":
            # change in call price over price of security
            if call:
                return N(T, t, sigma, S, K, r)
            else:
                # put-call symmetry
                # N(d1) - 1
                return N(T, t, sigma, S, K, r) - 1
    
        # change multiplier of call price over price of security
        elif greek == "gamma":
            # Same for both call and put (put-call parity)
            # 
            # 2nd order pde of call price with respect to spot price
            # N'(d1) / (S*sigma*sqrt(T-t))
            return 0
            
        # change in call price over std deviation
        elif greek == "vega":
            # Same for both call and put (put-call parity)
            # 
            # change in call price over std deviation
            # S*N'(d1)*sqrt(T-t)
            return 0
            
        # ** change in call price over time **
        elif greek == "theta":
            # change in call price over time
            if call:
                # theta = (-S*N'(d1)*sigma / 2sqrt(T-t)) - rKe^(-r(T-t)) * N(d2)
                return 0
            else:
                # theta = (-S*N'(d1)*sigma / 2sqrt(T-t)) - rKe^(-r(T-t)) * N(-d2)
                return 0
            
        # change in call price over annualized risk-free rate 
        elif greek == "rho":
            if call:
                # rho = K(T-t)*e^(-r*(T-t))*N(d2) 
                return 0
            else:
                # rho = -K(T-t)*e^(-r*(T-t))*N(-d2)  
                return 0
        
        return 0  
    