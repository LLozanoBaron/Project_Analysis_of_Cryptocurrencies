<h1 align="center"> PROYECTO INDIVIDUAL ANÁLISIS DE CRIPTOMONEDAS </h1>

## **INTRODUCCIÓN**

En este proyecto se van a analizar diez criptomonedas con menor volatilidad y por lo tanto aptas para inversiones a largo plazo, para determinar cuales criptomonedas se elegirian se realizo una busqueda en la web con el fin de comprender las mejores opciones de inversion para una empresa, con las monedas elegidas se realizo una limpieza y seleccion de datos con el fin de generar KPIs los cuales nos ayudaran a comprender las ganancias y a no generar perdidas con estas inversiones.

## **OBJETIVOS**

En este proyecto se tienen varios objetivos para completar el analisis:

+ Analizar mediante un EDA los datos seleccionados de las monedas.

+ Realizar el calculo del retorno de la inversion anual.

+ Determinar el punto de equilibrio real.

+ Calcular el margen de utilidad.

+ Presentar un dashboard en Power BI con el análisis.

## **Caracteristicas del proyecto**

Aqui se encuentran algunas de las mejores caracteristicas del proyecto:

+ Se realiza un análisis de las diez criptomonedas para inversion a largo plazo.
+ El proyecto utiliza una API especializada en criptomonedas, por lo tanto contiene datos actualizados.
+ Se muestra las ventajas economicas de la inversion.

## **Construcción del proyecto***

El proyecto fue construido con:
+ VSCode
+ Python 3.11.3
+ pyCoinGecko
+ Power BI
+ Excel

Los siguientes codigos son parte de la estructura del proyecto, los relacionados a las funciones de la API son de la autoria de pyCoinGecko:

+ El siguiente codigo se utilizo para instalar la API e importar todo lo necesario para realizar las consultas

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

+Con el siguiente codigo se selecciono las monedas por sus id y se conoce el nombre con el fin de tenerlos como variables

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

+ Con el siguiente codigo se obtine market cap y precios

```python
#Get the historical data of the coins
dataMarket_coins = cg.get_coins_markets(vs_currency= use_currencies,ids = id_coins,price_change_percentage = '24h,30d,1y',sparkline = True)
print(dataMarket_coins)

dfmarket_coins = pd.DataFrame.from_dict(dataMarket_coins).sort_values('id').reset_index(drop=True)
dfmarket_coins

dfmarket_filter = dfmarket_coins[['id','current_price','market_cap','market_cap_rank','fully_diluted_valuation','total_volume','high_24h','low_24h','price_change_24h','price_change_percentage_1y_in_currency','price_change_percentage_24h_in_currency','price_change_percentage_30d_in_currency']]
```

+ El siguiente es la obtención de los precios historicos de Bitcoin

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
+ También se hizo uso de Excel con el fin de que los precios fueran combinados de forma correcta y desde el 2021 hasta el 15 de agosto de 2023

## **Recursos**

+ https://github.com/man-c/pycoingecko.git
+ https://github.com/soyHenry/PI_DA.git
+ https://tradingplatforms.com/es/criptomonedas/criptomonedas-largo-plazo/
+ https://weareblox.com/es-es/criptomonedas-largo-plazo
+ https://admiralmarkets.com/es/education/articles/cryptocurrencies/mejores-criptomonedas-para-invertir
+ https://www.ig.com/es/ideas-de-trading-y-noticias/-cuales-son-las-6-mejores-criptomonedas-para-invertir-en-abril-2-230412

## **AUTORA**

Laura Viviana Lozano Baron

## **LICENCIA**

MIT
