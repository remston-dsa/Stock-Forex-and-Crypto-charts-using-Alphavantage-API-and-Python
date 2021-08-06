import streamlit as st


API_key='Z6P4MY41TAIKFAXW'

"""#TIMESERIES"""

def timeSeries(API_key, ticker):
  from alpha_vantage.timeseries import TimeSeries
  import matplotlib.pyplot as plt
  import mplfinance as mpf
  ts=TimeSeries(key=API_key, output_format='pandas')
  option=input('1. Intraday\n2. Daily\n3. Weekly\n4. Monthly\n5. Quote Endpoint\n6. Search Endpoint\n').lower()

  if option=='intraday' or option=='1':
    interval=int(input("Enter the interval:\n\t1. 1 minute\n\t2. 5 minutes\n\t3. 15 minutes\n\t4. 30 minutes\n\t5. 60 minutes\n"))
    inter=['','1min','5min','15min','30min','60min']
    data=ts.get_intraday(symbol=ticker, interval=inter[interval])[0]
    data.columns = ['Open', 'High', 'Low', 'Close', 'Volume']
    data.index.name = "Date"
    fig=mpf.plot(data,
             type='candle', 
             title=f"Intraday Time series for the {ticker} stock {inter[interval]}",
             mav=(20), 
             volume=True, 
             tight_layout=True,
             style='yahoo')
    st.plotly_chart(fig)
   
    return data

  elif option=='daily' or option=='2':
    data=ts.get_daily_adjusted(symbol=ticker)[0]
    data.columns = ['Open', 'High', 'Low', 'Close', 'Adjusted_close','Volume','Dividend Amount','Split Coefficient']
    data.index.name = "Date"
    mpf.plot(data,
             type='candle', 
             title=f'Daily Time series for the {ticker} stock',
             mav=(20), 
             volume=True, 
             tight_layout=True,
             style='yahoo')
    return data

  elif option=='weekly' or option=='3':
    data=ts.get_weekly_adjusted(symbol=ticker)[0]
    data.columns = ['Open', 'High', 'Low', 'Close', 'Adjusted_close','Volume','Dividend Amount']
    data.index.name = "Date"
    mpf.plot(data,
             type='candle', 
             title=f'Weekly Time series for the {ticker} stock',
             mav=(20), 
             volume=True, 
             tight_layout=True,
             style='yahoo')
    return data

  elif option=='monthly' or option=='4':
    data=ts.get_monthly_adjusted(symbol=ticker)[0]
    data.columns = ['Open', 'High', 'Low', 'Close', 'Adjusted_close','Volume','Dividend Amount']
    data.index.name = "Date"
    mpf.plot(data,
             type='candle', 
             title=f'Monthly Time series for the {ticker} stock',
             mav=(20), 
             volume=True, 
             tight_layout=True,
             style='yahoo')
    return data

  elif option=='quote endpoint' or option=='5':
    data=ts.get_quote_endpoint(symbol=ticker)[0]
    return data

  elif option=='search endpoint' or option=='6':
    keywords=input('Enter the Name of the Stock:\n')
    data=ts.get_symbol_search(keywords=keywords)[0]
    return data
    
  else:
    print("CANNOT RECOGNIZE")

timeSeries(API_key,'MSFT')

"""#FUNDAMENTAL DATA"""

def fundamentalData(API_key, ticker):
  from alpha_vantage.fundamentaldata import FundamentalData
  import matplotlib.pyplot as plt

  fd=FundamentalData(key=API_key, output_format='pandas')
  option=input('1. Company Overview\n2. Earnings\n3. Income Statement\n4. Balance Sheet\n5. Cash Flow\n6. Listing Status\n7. Earnings Calendar\n8. IPO calandar\n').lower()
  
  if option=='company overview' or option=='1':
    data=fd.get_company_overview(symbol=ticker)[0]
    return data

  elif option=='earnings' or option=='2':
    data=fd.get_earnings(symbol=ticker)
    return data

  elif option=='income statement' or option=='3':
    period=input("1. Annual\n2. Quaterly\n").lower()
    if period=='annual' or period=='1':
      data=fd.get_income_statement_annual(symbol=ticker)[0].T
      return data
    elif period=='quaterly' or period=='2':
      data=fd.get_income_statement_quaterly(symbol=ticker)[0].T
      return data
    else:
      print("No data available")

  elif option=='balance sheet' or option=='4':
    period=input("1. Annual\n2. Quaterly\n").lower()
    if period=='annual' or period=='1':
      data=fd.get_balance_sheet_annual(symbol=ticker)[0].T
      return data
    elif period=='quaterly' or period=='2':
      data=fd.get_balance_sheet_quaterly(symbol=ticker)[0].T
      return data
    else:
      print("No data available")

  elif option=='cash flow' or option=='5':
    period=input("1. Annual\n2. Quaterly\n").lower()
    if period=='annual' or period=='1':
      data=fd.get_cash_flow_annual(symbol=ticker)[0].T
      return data
    elif period=='quaterly' or period=='2':
      data=fd.get_cash_flow_quaterly(symbol=ticker)[0].T
      return data
    else:
      print("No data available")

  elif option=='listing status' or option=='6':
    data=fd.get_listing_status()
    return data

  elif option=='earnings calendar' or option=='7':
    data=fd.get_earnings_calendar()

  elif option=='ipo calendar' or option=='8':
    data=fd.get_ipo_calendar()

  else:
    print("CANNOT RECOGNIZE")

fundamentalData(API_key, 'MSFT')

"""#TECHNICAL INDICATORS

"""

def technicalIndicators(API_key,ticker):
  from alpha_vantage.techindicators import TechIndicators
  import matplotlib.pyplot as plt
  import mplfinance as mpf

  ti=TechIndicators(key=API_key, output_format='pandas')
  option=input('1. SMA\n2. EMA\n3. VWAP\n4. MACD\n5. STOCH\n6. RSI\n7. ADX\n8. CCI\n9. AROON\n10. BBANDS\n11. AD\n12. OBV\n').lower()

  if option=='sma' or option=='1':
    interval=int(input("Enter the interval:\n\t1. 1 minute\n\t2. 5 minutes\n\t3. 15 minutes\n\t4. 30 minutes\n\t5. 60 minutes\n\t6. daily \n\t7. weekly\n\t8. monthly\n"))
    intervalList=['','1min','5min','15min','30min','60min','daily','weekly','monthly']
    timeperiod=int(input('Enter Time Period\n'))
    ser=int(input('Enter the series:\n\t1. close\n\t2. open\n\t3. low\n\t4. high\n'))
    series=['','close','open','low','high']
    data=ti.get_sma(symbol=ticker, interval=intervalList[interval], time_period=timeperiod, series_type=series[ser])[0]
    data.columns = ['SMA']
    data.index.name ="Date"
    mpf.plot(data,
             type='candle', 
             title=f'SMA for the {ticker} stock',
             mav=(20), 
             volume=True, 
             tight_layout=True,
             style='yahoo')
    mpf.plot(data,type='line', volume=True)
    return data
    
  elif option=='ema' or option=='2':
    interval=int(input("Enter the interval:\n\t1. 1 minute\n\t2. 5 minutes\n\t3. 15 minutes\n\t4. 30 minutes\n\t5. 60 minutes\n\t6. daily \n\t7. weekly\n\t8. monthly\n"))
    intervalList=['','1min','5min','15min','30min','60min','daily','weekly','monthly']
    timeperiod=int(input('Enter Time Period\n'))
    ser=int(input('Enter the series:\n\t1. close\n\t2. open\n\t3. low\n\t4. high\n'))
    series=['','close','open','low','high']
    data=ti.get_ema(symbol=ticker, interval=intervalList[interval], time_period=timeperiod, series_type=series[ser])[0]
    data.plot()
    plt.title(f'EMA for the {ticker} stock')
    plt.tight_layout()
    plt.grid()
    plt.show()
    return data

  elif option=='vwap' or option=='3':
    interval=int(input("Enter the interval:\n\t1. 1 minute\n\t2. 5 minutes\n\t3. 15 minutes\n\t4. 30 minutes\n\t5. 60 minutes\n"))
    intervalList=['','1min','5min','15min','30min','60min']
    data=ti.get_vwap(symbol=ticker, interval=intervalList[interval])[0]
    data.plot()
    plt.title(f'VWAP for the {ticker} stock')
    plt.tight_layout()
    plt.grid()
    plt.show()
    return data

  elif option=='macd' or option=='4':
    interval=int(input("Enter the interval:\n\t1. 1 minute\n\t2. 5 minutes\n\t3. 15 minutes\n\t4. 30 minutes\n\t5. 60 minutes\n\t6. daily \n\t7. weekly\n\t8. monthly\n"))
    intervalList=['','1min','5min','15min','30min','60min','daily','weekly','monthly']
    ser=int(input('Enter the series:\n\t1. close\n\t2. open\n\t3. low\n\t4. high\n'))
    series=['','close','open','low','high']
    data=ti.get_macd(symbol=ticker, interval=intervalList[interval], series_type=series[ser])[0]
    data.plot()
    plt.title(f'MACD for the {ticker} stock')
    plt.tight_layout()
    plt.grid()
    plt.show()
    return data

  elif option=='stoch' or option=='5':
    interval=int(input("Enter the interval:\n\t1. 1 minute\n\t2. 5 minutes\n\t3. 15 minutes\n\t4. 30 minutes\n\t5. 60 minutes\n\t6. daily \n\t7. weekly\n\t8. monthly\n"))
    intervalList=['','1min','5min','15min','30min','60min','daily','weekly','monthly']
    data=ti.get_stoch(symbol=ticker, interval=intervalList[interval])[0]
    data.plot()
    plt.title(f'STOCH for the {ticker} stock')
    plt.tight_layout()
    plt.grid()
    plt.show()
    return data

  elif option=='rsi' or option=='6':
    interval=int(input("Enter the interval:\n\t1. 1 minute\n\t2. 5 minutes\n\t3. 15 minutes\n\t4. 30 minutes\n\t5. 60 minutes\n\t6. daily \n\t7. weekly\n\t8. monthly\n"))
    intervalList=['','1min','5min','15min','30min','60min','daily','weekly','monthly']
    timeperiod=int(input('Enter Time Period\n'))
    ser=int(input('Enter the series:\n\t1. close\n\t2. open\n\t3. low\n\t4. high\n'))
    series=['','close','open','low','high']
    data=ti.get_rsi(symbol=ticker, interval=intervalList[interval], time_period=timeperiod, series_type=series[ser])[0]
    data.plot()
    plt.title(f'RSI for the {ticker} stock')
    plt.tight_layout()
    plt.grid()
    plt.show()
    return data

  elif option=='adx' or option=='7':
    interval=int(input("Enter the interval:\n\t1. 1 minute\n\t2. 5 minutes\n\t3. 15 minutes\n\t4. 30 minutes\n\t5. 60 minutes\n\t6. daily \n\t7. weekly\n\t8. monthly\n"))
    intervalList=['','1min','5min','15min','30min','60min','daily','weekly','monthly']
    timeperiod=int(input('Enter Time Period\n'))
    data=ti.get_adx(symbol=ticker, interval=intervalList[interval], time_period=timeperiod)[0]
    data.plot()
    plt.title(f'ADX for the {ticker} stock')
    plt.tight_layout()
    plt.grid()
    plt.show()
    return data

  elif option=='cci' or option=='8':
    interval=int(input("Enter the interval:\n\t1. 1 minute\n\t2. 5 minutes\n\t3. 15 minutes\n\t4. 30 minutes\n\t5. 60 minutes\n\t6. daily \n\t7. weekly\n\t8. monthly\n"))
    intervalList=['','1min','5min','15min','30min','60min','daily','weekly','monthly']
    timeperiod=int(input('Enter Time Period\n'))
    data=ti.get_cci(symbol=ticker, interval=intervalList[interval], time_period=timeperiod)[0]
    data.plot()
    plt.title(f'CCI for the {ticker} stock')
    plt.tight_layout()
    plt.grid()
    plt.show()
    return data

  elif option=='aroon' or option=='9':
    interval=int(input("Enter the interval:\n\t1. 1 minute\n\t2. 5 minutes\n\t3. 15 minutes\n\t4. 30 minutes\n\t5. 60 minutes\n\t6. daily \n\t7. weekly\n\t8. monthly\n"))
    intervalList=['','1min','5min','15min','30min','60min','daily','weekly','monthly']
    timeperiod=int(input('Enter Time Period'))
    data=ti.get_aroon(symbol=ticker, interval=intervalList[interval], time_period=timeperiod)[0]
    data.plot()
    plt.title(f'AROON for the {ticker} stock')
    plt.tight_layout()
    plt.grid()
    plt.show()
    return data
    
  elif option=='bbands' or option=='10':
    interval=int(input("Enter the interval:\n\t1. 1 minute\n\t2. 5 minutes\n\t3. 15 minutes\n\t4. 30 minutes\n\t5. 60 minutes\n\t6. daily \n\t7. weekly\n\t8. monthly\n"))
    intervalList=['','1min','5min','15min','30min','60min','daily','weekly','monthly']
    timeperiod=int(input('Enter Time Period\n'))
    ser=int(input('Enter the series:\n\t1. close\n\t2. open\n\t3. low\n\t4. high\n'))
    series=['','close','open','low','high']
    data=ti.get_bbands(symbol=ticker, interval=intervalList[interval], time_period=timeperiod, series_type=series[ser])[0]
    data.plot()
    plt.title(f'BBANDS for the {ticker} stock')
    plt.tight_layout()
    plt.grid()
    plt.show()
    return data

  elif option=='ad' or option=='11':
    interval=int(input("Enter the interval:\n\t1. 1 minute\n\t2. 5 minutes\n\t3. 15 minutes\n\t4. 30 minutes\n\t5. 60 minutes\n\t6. daily \n\t7. weekly\n\t8. monthly\n"))
    intervalList=['','1min','5min','15min','30min','60min','daily','weekly','monthly']
    data=ti.get_ad(symbol=ticker, interval=intervalList[interval])[0]
    data.plot()
    plt.title(f'AD for the {ticker} stock')
    plt.tight_layout()
    plt.grid()
    plt.show()
    return data

  elif option=='obv' or option=='12':
    interval=int(input("Enter the interval:\n\t1. 1 minute\n\t2. 5 minutes\n\t3. 15 minutes\n\t4. 30 minutes\n\t5. 60 minutes\n\t6. daily \n\t7. weekly\n\t8. monthly\n"))
    intervalList=['','1min','5min','15min','30min','60min','daily','weekly','monthly']
    data=ti.get_obv(symbol=ticker, interval=intervalList[interval])[0]
    data.plot()
    plt.title(f'OBV for the {ticker} stock')
    plt.tight_layout()
    plt.grid()
    plt.show()
    return data

  else:
    print("CANNOT RECOGNIZE")

technicalIndicators(API_key,'MSFT')

"""#FOREX"""

def forex(API_key, fromCurr, toCurr):
  from alpha_vantage.foreignexchange import ForeignExchange
  import matplotlib.pyplot as plt

  fe=ForeignExchange(key=API_key,output_format='pandas')
  option=input('1. Exchange Rates\n2. Intraday\n3. Daily\n4. Weekly\n5. Monthly\n').lower()

  if option=='exchange rates' or option=='1':
    data=fe.get_currency_exchange_rate(from_currency=fromCurr, to_currency=toCurr)[0]
    return data

  elif option=='intraday' or option=='2':
    interval=int(input("Enter Interval:\n\t1. 1 minute\n\t2. 5 minutes\n\t3. 15 minutes\n\t4. 30 minutes\n\t5. 60 minutes\n"))
    intervalList=['','1min','5min','15min','30min','60min']
    data=fe.get_currency_exchange_intraday(from_symbol=fromCurr, to_symbol=toCurr,interval=intervalList[interval])[0]
    data.plot()
    plt.title(f'Forex Intraday for the {fromCurr}-{toCurr} stock ({intervalList[interval]})')
    plt.tight_layout()
    plt.grid()
    plt.show()
    return data

  elif option=='daily' or option=='3':
    data=fe.get_currency_exchange_daily(from_symbol=fromCurr, to_symbol=toCurr)[0]
    data.plot()
    plt.title(f'Forex Daily for the {fromCurr}-{toCurr} stock')
    plt.tight_layout()
    plt.grid()
    plt.show()
    return data

  elif option=='weekly' or option=='4':
    data=fe.get_currency_exchange_weekly(from_symbol=fromCurr, to_symbol=toCurr)[0]
    data.plot()
    plt.title(f'Forex Weekly for the {fromCurr}-{toCurr} stock')
    plt.tight_layout()
    plt.grid()
    plt.show()
    return data

  elif option=='monthly' or option=='5':
    data=fe.get_currency_exchange_monthly(from_symbol=fromCurr, to_symbol=toCurr)[0]
    data.plot()
    plt.title(f'Forex Monthly for the {fromCurr}-{toCurr} stock')
    plt.tight_layout()
    plt.grid()
    plt.show()
    return data
  else:
    print("DATA NOT AVAILABLE")

forex(API_key, 'USD', 'INR')

"""#CRYPTOCURRENCY

"""

def cryptocurrency(API_key, currency):
  from alpha_vantage.cryptocurrencies import CryptoCurrencies
  import matplotlib.pyplot as plt

  cc=CryptoCurrencies(key=API_key,output_format='pandas')
  option=input('1. Exchange Rates\n2. Health Index\n3. Daily\n4. Weekly\n5. Monthly\n').lower()

  if option=='exchange rates' or option=='1':
    data=cc.get_currency_exchange_rate(from_currency=currency, to_currency='USD')[0]
    return data

  elif option=='health index' or option=='2':
    data=cc.get_crypto_rating(symbol=currency)[0]
    return data

  elif option=='daily' or option=='3':
    data=cc.get_digital_currency_daily(symbol=currency, market='CNY')[0]
    data.plot()
    plt.title(f'Crypto Daily for the {currency} stock')
    plt.tight_layout()
    plt.grid()
    plt.show()
    return data

  elif option=='weekly' or option=='4':
    data=cc.get_digital_currency_weekly(symbol=currency, market='CNY')[0]
    data.plot()
    plt.title(f'Crypto Weekly for the {currency} stock')
    plt.tight_layout()
    plt.grid()
    plt.show()
    return data

  elif option=='monthly' or option=='5':
    data=cc.get_digital_currency_monthly(symbol=currency, market='CNY')[0]
    data.plot()
    plt.title(f'Crypto Monthly for the {currency} stock')
    plt.tight_layout()
    plt.grid()
    plt.show()
    return data
  else:
    print("DATA NOT AVAILABLE")

cryptocurrency(API_key, 'BTC')
