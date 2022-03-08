# %%
!pip install yfinance
!pip install pandas 
!pip install matplotlib
!pip install seaborn

# %%
import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# %%
data = yf.download(['msft','rblx','nvda'], start='2020-01-01',end='2022-01-01')
price = data['Close']
opn = data['Open']
chg = price - opn
# %%
chg.columns
# %%
price.plot.area(title='Price of Stocks in USD',ylabel='USD',xlabel='date')
# %%
data.plot.area(legend=None)
# %%
!pip install talib


# %%
import talib
# %%
