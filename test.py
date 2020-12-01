#!/mnt/c/Users/Qi/Documents/alpha/virenv/bin/python3


import pandas as pd
from pypfopt.efficient_frontier import EfficientFrontier
from pypfopt import risk_models
from pypfopt import expected_returns

# Read in price data
addr = "/mnt/c/Users/Qi/Downloads/PyPortfolioOpt-master/tests/resources/stock_prices.csv"
df = pd.read_csv(addr, parse_dates=True, index_col="date")

# Calculate expected returns and sample covariance
mu = expected_returns.mean_historical_return(df)
S = risk_models.sample_cov(df)

# Optimise for maximal Sharpe ratio
ef = EfficientFrontier(mu, S)
weights = ef.max_sharpe()
ef.portfolio_performance(verbose=True)
