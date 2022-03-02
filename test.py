# %%
!pip install mplfinance
!pip install finta
!pip install yfinance

# %%
import yfinance as yf, mplfinance as mpf, finta as fta, numpy as np, matplotlib.pyplot as plt
from finta import TA
slow = '20d'
fast = '8d'
efoi = yf.download('efoi',period='1y', interval='1d')
amd = yf.download('amd',period='1y',interval='1d')


# %%

amd['s_ema'] = TA.EMA(amd, 24)
amd['f_ema'] = TA.EMA(amd, 12)
amd['Signal'] = 0.0
amd['Signal'] = np.where(amd['s_ema'] > amd['f_ema'], 1.0, 0.0)
amd['Position'] = amd['Signal'].diff()
amd[['s_ema','f_ema','Close']].plot.line()

# %%
 amd['Signal'].diff()

# %%
plt.figure(figsize = (20,10))
# plot Close, short-term and long-term moving averages 
amd['Close'].plot(color = 'y', label= 'Close') 
amd['f_ema'].plot(color = 'b',label = '8-day SMA') 
amd['s_ema'].plot(color = 'g', label = '20-day EMA')# plot ‘buy’ signals
plt.plot(amd[amd['Position'] == 1].index, 
         amd['f_ema'][amd['Position'] == 1], 
         'v', markersize = 15, color = 'r', label = 'sell')# plot ‘sell’ signals
plt.plot(amd[amd['Position'] == -1].index, 
         amd['f_ema'][amd['Position'] == -1], 
         '^', markersize = 15, color = 'g', label = 'buy')
plt.ylabel('Price in USD', fontsize = 15 )
plt.xlabel('Date', fontsize = 15 )
plt.title('AMD', fontsize = 20)
plt.legend()
plt.grid()
plt.show()

# %%
bbands = TA.BBANDS(amd)
efoi_df = mpf.plotting.make_addplot(efoi)
amd_df = mpf.plotting.make_addplot(amd)

# %%


# %%
bbands = bbands.fillna(0)

# %%
amd.isna().sum()


# %%
figure = plt.figure()
amd[100:][['BB_Upper','BB_Middle','BB_Lower']]= bbands
plt.savefig('BB_Bands.png')
# %%
mpf.plot(amd)

# %%
amd[['BB_Upper','BB_Lower','Close']].plot.line()
