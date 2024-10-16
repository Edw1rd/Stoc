import quantstats as qs

stock ="SPY"

portfolio = qs.utils.download_returns(stock, period='3y')

print(f"Sharpe: {qs.stats.sharpe(portfolio)}")
print(f"Best Day: {qs.stats.best(portfolio)}")
print(f"Best Day: {qs.stats.best(portfolio, aggregate='M')}")

qs.extend_pandas()

print(portfolio.cagr())
print(portfolio.max_drawdown())
print(portfolio.monthly_returns())