<h1 align="center"> INDIVIDUAL PROJECT ANALYSIS OF CRYPTOCURRENCIES </h1>

## **INTRODUCTION**

In this project, ten cryptocurrencies with lower volatility and therefore suitable for long-term investments will be analyzed. To determine which cryptocurrencies would be chosen, a web search was conducted to understand the best investment options for a company. With the chosen coins, data cleaning and selection were carried out to generate KPIs that will help us understand the gains and losses that will be incurred if the decision is made to continue with this investment.

## **OBJECTIVES**

EIn this project, there are several objectives to complete the analysis:

+ Analyze the selected data from the coins through an EDA.

+ Calculate the annual return on investment.

+ Determine the actual break-even point.

+ Calculate the profit margin.

+ Present a dashboard in Power BI with the analysis.

## **THE CHARACTERISTICS OF THE PROJECT**

Here are some of the best features of the project:

+ An analysis of the ten cryptocurrencies for long-term investment is carried out.
+ The project uses a specialized cryptocurrency API, therefore it contains updated data.
+ It can be determined through analysis that the return on investment in cryptocurrencies such as Solana and Ethereum, to name just two, is much higher than that of Bitcoin in the last year
+ Interpreting the profit margin, if an investment of $60,000 is made in cryptocurrencies, there is a profit of 91.77%, indicating that they are highly profitable investments
+ It was determined that the break-even points are acceptable because many of these cryptocurrencies are of low value and high profitability.

## **Construction of the project***

he project was built with:
+ VSCode
+ Python 3.11.3
+ Pandas, Numpy, Matplotlib,Seaborn
+ pyCoinGecko
+ Power BI
+ Microsoft Excel
+ Different specialized web pages, which provided information on the least volatile currencies.

The following codes are part of the project structure, those related to the API functions are authored by pyCoinGecko:

+ The following code was used to install the API and import everything necessary to perform the queries.

``` python
pip install pycoingecko
pip install plotly

import pandas as pd
import datetime as dt
import time as t
import numpy as np
import plotly.graph_objects as go
from plotly.offline import plot
from pycoingecko import CoinGeckoAPI
import matplotlib.pyplot as plt
import seaborn as sns

from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()

cg.ping()  
```

+ With the following code, the coins were selected by their id and the name is known in order to have them as variables.

```python
#df_coin[df_coin['id'] == 'bitcoin']
#df_coin[df_coin['id'] == 'chainlink']
#df_coin[df_coin['id'] == 'ethereum']
#df_coin[df_coin['id'] == 'ripple']
#df_coin[df_coin['id'] == 'solana']
#df_coin[df_coin['id'] == 'litecoin']
#df_coin[df_coin['id'] == 'dogecoin']
#df_coin[df_coin['id'] == 'uniswap']
#df_coin[df_coin['id'] == 'polkadot']
#df_coin[df_coin['id'] == 'cardano']

coins = ['Bitcoin','Ethereum','XRP','Solana','Litecoin','Dogecoin','Uniswap','Polkadot','Cardano','Chainlink']

id_coins = ['bitcoin','chainlink','ethereum','ripple','solana','litecoin','dogecoin','uniswap','polkadot','cardano']

#get the currencies
currencies = cg.get_supported_vs_currencies()
use_currencies = 'usd'
```

+ With the following code, market cap and prices are obtained.

```python
#Get the historical data of the coins
dataMarket_coins = cg.get_coins_markets(vs_currency= use_currencies,ids = id_coins,price_change_percentage = '24h,30d,1y',sparkline = True)
print(dataMarket_coins)

dfmarket_coins = pd.DataFrame.from_dict(dataMarket_coins).sort_values('id').reset_index(drop=True)
dfmarket_coins

dfmarket_filter = dfmarket_coins[['id','current_price','market_cap','market_cap_rank','fully_diluted_valuation','total_volume','high_24h','low_24h','price_change_24h','price_change_percentage_1y_in_currency','price_change_percentage_24h_in_currency','price_change_percentage_30d_in_currency']]
```

+ The following is the obtaining of the historical prices of Bitcoin.

```python
#get daily historical data
daily_bitcoin = cg.get_coin_market_chart_by_id(id = 'bitcoin', 
                               vs_currency = 'usd',
                               days = 'max')

#input a range of timestamps to get data for - using predetermined frequency
chartRange_bitcoin = cg.get_coin_market_chart_range_by_id(id = 'bitcoin', 
                                                  vs_currency = 'usd', 
                                                  from_timestamp = 1577854800, 
                                                  to_timestamp = 1703998800)
#list of lists to dataframe 
df_hist_bitcoin = pd.DataFrame(data = daily_bitcoin['prices'],
                                        columns = ['Date', 'Price bitcoin'])
#reformat date
df_hist_bitcoin['Date'] = df_hist_bitcoin['Date'].apply(
             lambda x: dt.datetime.fromtimestamp(x/1000).strftime('%d-%m-%Y'))
#set index
df_hist_bitcoin = df_hist_bitcoin.set_index('Date')

print(df_hist_bitcoin)

#Plot

fig, ax = plt.subplots(figsize=(15, 5))
df_hist_bitcoin['Price bitcoin'].plot(ax=ax)
ax.set_title('Bitcoin Price History')
plt.show()
```
+ Excel was also used in order to combine the prices correctly and from 2021 until August 15, 2023.

## **RESOURCES**

+ https://github.com/man-c/pycoingecko.git
+ https://github.com/soyHenry/PI_DA.git
+ https://tradingplatforms.com/es/criptomonedas/criptomonedas-largo-plazo/
+ https://weareblox.com/es-es/criptomonedas-largo-plazo
+ https://admiralmarkets.com/es/education/articles/cryptocurrencies/mejores-criptomonedas-para-invertir
+ https://www.ig.com/es/ideas-de-trading-y-noticias/-cuales-son-las-6-mejores-criptomonedas-para-invertir-en-abril-2-230412

## **AUTHOR**

Laura Viviana Lozano Baron

## **LICENSE**

This work is under the MIT liecense.
