import tkinter as tk
import pandas as pd
from matplotlib.figure import Figure
from PIL import ImageTk, Image

root = tk.Tk()
root.title("Finance Info Engine ")

root.geometry('1400x800')
def timeSeries(API_key='Z6P4MY41TAIKFAXW', ticker="MSFT"):
    from alpha_vantage.timeseries import TimeSeries
    import matplotlib.pyplot as plt
    import mplfinance as mpf
    ts = TimeSeries(key=API_key, output_format='pandas')
    data = ts.get_daily_adjusted(symbol=ticker)[0]
    data.columns = ['Open', 'High', 'Low', 'Close', 'Adjusted_close', 'Volume', 'Dividend Amount', 'Split Coefficient']
    data.index.name = "Date"
    mpf.plot(data,
             type='candle',
             title=f'Daily Time series for the {ticker} stock',
             mav=(20),
             volume=True,
             tight_layout=True,
             style='yahoo',
             savefig='stock.png')
    
  
    img = ImageTk.PhotoImage(Image.open('stock.png'))
    frame1=tk.Frame(root,height=590,width=800,bg="white")
    panel = tk.Label(frame1, image=img)
    panel.place(x=0,y=0)
    frame1.place(x=250,y=100)
    l1 = tk.Label(root,
                  text="hey!.\n Now you entered right stock name \n Thank you  ",
                  fg="green", font=("lucida", 10, "bold"))
    l1.place(x=20, y=200)

    return data


def forex(API_key='Z6P4MY41TAIKFAXW', fromCurr='INR', toCurr='USD'):
    from alpha_vantage.foreignexchange import ForeignExchange
    import matplotlib.pyplot as plt
    import mplfinance as mpf

    fe = ForeignExchange(key=API_key, output_format='pandas')
    data = fe.get_currency_exchange_daily(from_symbol=fromCurr, to_symbol=toCurr)[0]

    a = data["4. close"].iloc[0]
    return a
inf1=forex(API_key='Z6P4MY41TAIKFAXW', fromCurr="USD", toCurr='INR')

def cryptocurrency(API_key='Z6P4MY41TAIKFAXW', currency="BTC"):

    from alpha_vantage.cryptocurrencies import CryptoCurrencies
    import matplotlib.pyplot as plt
    import mplfinance as mpf

    cc = CryptoCurrencies(key=API_key, output_format='pandas')
    data = cc.get_digital_currency_daily(symbol=currency, market='INR')[0]


    b= data["1a. open (INR)"].iloc[0]
    return b
inf2=cryptocurrency(API_key='Z6P4MY41TAIKFAXW', currency="BTC")

def sectorPerformance(API_key='Z6P4MY41TAIKFAXW'):

    from alpha_vantage.sectorperformance import SectorPerformances
    import matplotlib.pyplot as plt
    import mplfinance as mpf

    sp = SectorPerformances(key=API_key, output_format='pandas')
    data = sp.get_sector()[0]
    a=data.index[0]
    return a




def incorr():
    l1=tk.Label(root,text="INVALID INPUT!.\n Please enter correct stock name \n Please check for spelling mistakes and etc",fg="black",font=("lucida",10,"bold"))
    l1.place(x=20,y=200)

inf3=sectorPerformance(API_key='Z6P4MY41TAIKFAXW')

def quote(API_key='Z6P4MY41TAIKFAXW',ticker='SPY'):
  from alpha_vantage.timeseries import TimeSeries
  ts=TimeSeries(key=API_key, output_format='pandas')
  
  data=ts.get_quote_endpoint(symbol=ticker)[0]
  ind=data['05. price'].iloc[0]
  return ind

inf4=quote(API_key='Z6P4MY41TAIKFAXW',ticker='SPY')
inf5=quote(API_key='Z6P4MY41TAIKFAXW',ticker='DIA')
def submit1():
    a=textbox.get()
    try:
        timeSeries(API_key='Z6P4MY41TAIKFAXW', ticker=a)
    except ValueError:
        incorr()
    except AttributeError:
        incorr()




heading=tk.Label(root,text="Finance Info Engine",fg="red",font=("lucida",35,"bold"))
heading.place(x=400, y=3)

textbox=tk.Entry(root,borderwidth=0.5, relief="solid",font=("lucida",14,"bold"))
textbox.place(x=20,y=110)

submit_button=tk.Button(root,text="submit",font=("ariel",14,"bold"),fg="red",borderwidth=1, relief="solid",command=submit1)
submit_button.place(x=20,y=150)

latest_info=tk.Label(root,text="Latest info",fg="green",font=("ariel",25,"bold"))
latest_info.place(x=1100, y=110)


info1=tk.Label(root,text=f"USD/INR- {inf1}",fg="red",bg="yellow",font=("ariel",15,"bold"),borderwidth=1, relief="solid")
info1.place(x=1100, y=180)
info2=tk.Label(root,text=f"BTC/INR- {inf2}",fg="red",bg="yellow",font=("ariel",15,"bold"),borderwidth=1, relief="solid")
info2.place(x=1100, y=240)
info3=tk.Label(root,
text=f'''BEST PERFORMING SECTOR
- {inf3}''',bg="light pink",fg="red",font=("ariel",12,"bold"),borderwidth=1, relief="solid")
info3.place(x=1100, y=300)
info4=tk.Label(root,text=f"S&P 500- {inf4}",fg="red",font=("ariel",15,"bold"),borderwidth=1, relief="solid")
info4.place(x=1100, y=380)
info5=tk.Label(root,text=f"DOW JONES- {inf5}",fg="red",font=("ariel",15,"bold"),borderwidth=1, relief="solid")
info5.place(x=1100, y=440)

chartinfo=tk.Label(root,text="One Day Chart",fg="red",font=("lucida",20,"bold"))
chartinfo.place(x=400, y=650)

root.configure(bg="white")


root.mainloop()
