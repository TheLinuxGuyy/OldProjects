import smtplib
import ssl
from bs4 import BeautifulSoup
from lxml import etree
from numpy.core.fromnumeric import trace
import requests
import time
import lxml
import datetime
import lxml
import threading
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
import numpy as np
import pandas_datareader as web
import datetime as dt
from selenium.webdriver.chrome.options import Options as ChromeOptions
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.layers import Dense,Dropout,LSTM
from tensorflow.keras.models import Sequential
from lxml import etree
from email.message import EmailMessage
import asyncio
from urllib.request import Request, urlopen
from urllib.request import urlparse as urljoin
from bs4 import BeautifulSoup
from bs4.element import Comment 
from bs4 import BeautifulSoup as bs
import lxml
from datetime import datetime
import socket
import pandas as pd
from selenium.webdriver.chrome.service import Service
import websockets
from selenium import webdriver
import asyncio
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
future_day=2
gettingdaysforpred=requests.get('https://www.calendardate.com/todays.htm').text
gettingdaysforpred=BeautifulSoup(gettingdaysforpred,'lxml')
gettingdaysforpred=gettingdaysforpred.find_all('td', colspan="9", align="CENTER")
gettingdaysforpred=gettingdaysforpred[0]
gettingdaysforpred=str(gettingdaysforpred)
gettingdaysforpred=gettingdaysforpred.replace('<td align="CENTER" colspan="9">','').replace('2022</td>','')
weekdays=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday','Monday']
months=['January','February','March','April','May','June','July','August','September','October','November','December']
cryp="Cardano"
csubject="CRYPTO STOCK INFO (Cardano)"
myemail="cryptobot693@gmail.com"
recvemail="clivethompson09@gmail.com"
password="----------"
chrome_options=ChromeOptions()
PATH="C:/Users/clive/Downloads/chromedriver.exe"
options=ChromeOptions()
options.add_argument("--headless")
driver=webdriver.Chrome(PATH)
driver.get("https://www.coingecko.com")
tr=driver.page_source
tr=BeautifulSoup(tr,"lxml")
tr=tr.find_all("a", class_="d-lg-none font-bold tw-w-12")
tr=list(tr)
tr=tr[:50]
comparevals=[]
cryptonameslist=[]
allcryptolist=[]
numdict={}
class Stock:
    def price_pred(self,crypto_name,crypto_currnecy,*args):
        global predictionlist
        predictionlist=[]
        global arg
        global crypt_name
        arg=args
        allsfincrypt.append(crypto_name.replace('-','_'))
        global outside_crypto_name
        outside_crypto_name=crypto_name
        while True:
            try:
                driver.get(f'https://www.coingecko.com/en/coins/{crypto_name}/eur')
                break
            except:
                pass
        cpage=driver.page_source
        csoup=BeautifulSoup(cpage,"lxml")
        global cres
        cres=csoup.find_all('span', class_="no-wrap")
        cplusressuop=BeautifulSoup(cpage,"html.parser")
        dom=etree.HTML(str(cplusressuop))
        against_currency='EUR'
        check=False
        try:
            data=web.DataReader(f'{crypto_currnecy}-{against_currency}',data_source='yahoo')
        except:
            try:
                data=web.DataReader(f'{crypto_currnecy}-USD',data_source='yahoo')
            except:
                return
            check=True

        for line in args:      
            scaler=MinMaxScaler(feature_range=(0,1))
            scaled_data=scaler.fit_transform(data['Close'].values.reshape(-1,1))
            prediction_days=60
            x_train,y_train=[],[]
            for x in range(prediction_days,len(scaled_data)-line):
                x_train.append(scaled_data[x-prediction_days:x,0])
                y_train.append(scaled_data[x+line,0])
            x_train,y_train=np.array(x_train),np.array(y_train)
            x_train=np.reshape(x_train, (x_train.shape[0],x_train.shape[1],1))
            model=Sequential()
            model.add(LSTM(units=50,return_sequences=True,input_shape=(x_train.shape[1],1)))
            model.add(Dropout(0.2))
            model.add(LSTM(units=50,return_sequences=True))
            model.add(Dropout(0.2))
            model.add(LSTM(units=50))
            model.add(Dense(units=1))
            model.compile(optimizer='adam',loss='mean_squared_error')
            model.fit(x_train,y_train,epochs=50,batch_size=32)
            if check:
                test_data=web.DataReader(f'{crypto_currnecy}-USD',data_source='yahoo')
            else:
                test_data=web.DataReader(f'{crypto_currnecy}-{against_currency}',data_source='yahoo')
            actual_prices=test_data['Close'].values
            total_dataset=pd.concat((data['Close'],test_data['Close']),axis=0)
            model_inputs=total_dataset[len(total_dataset)-len(test_data) -prediction_days:].values
            model_inputs=model_inputs.reshape(-1,1)
            model_inputs=scaler.fit_transform(model_inputs)
            x_test=[]
            for x in range(prediction_days,len(model_inputs)):
                x_test.append(model_inputs[x-prediction_days:x,0])
            x_test=np.array(x_test)
            x_test=np.reshape(x_test,(x_test.shape[0],x_test.shape[1],1))
            prediction_prices=model.predict(x_test)
            prediction_prices=scaler.inverse_transform(prediction_prices)
            #threading.Thread(target=plt.show()).start()
            real_data = [model_inputs[len(model_inputs) - prediction_days : len(model_inputs)+1, 0]]
            real_data=np.array(real_data)
            real_data=np.reshape(real_data,(real_data.shape[0],real_data.shape[1],1))
            prediction=model.predict(real_data)
            prediction=scaler.inverse_transform(prediction)
            prediction=str(prediction)
            prediction=prediction.replace('[[','')
            prediction=prediction.replace(']]','')
            cryptonameslist.append(crypto_name)
            print(cres[0].text)
            global crypt_name
            crypt_name=crypto_name.replace("-","_")
            r=f"global {crypt_name}_compred"
            print(r)
            exec(r)
            serbr
            cres[0]=cres[0].text.replace(",","")
            exeuteablecompare=f"{crypt_name}_compred=float({cres[0][1:]})-float({prediction})"
            exec(exeuteablecompare)
            rtfwafwfaawf=f"self.{crypt_name}_predictionn=float({prediction})"
            exec(rtfwafwfaawf)
            exeuteablecompare=f"print({crypt_name}_compred)"
            exec(exeuteablecompare)
            exeuteablecompare=f"comparevals.append({crypt_name}_compred)"
            exec(exeuteablecompare)
            if line==args[0]:
                exeuteablecompare=f"self.{crypt_name}_list=[]"
                exec(exeuteablecompare)
            exeuteablecompare=f"self.{crypt_name}_list.append({crypt_name}_compred)"
            exec(exeuteablecompare)
            treingesx="print(f'self.{crypt_name}_list')"
            exec(treingesx)
            cryptss_name=crypt_name.replace("_"," ")
            if line==args[::-1][0]:
                global cbody
                Ys=crypt_name+"cbody"
                x=f'self.{Ys}="{cryptss_name} price: {cres[0]} (24h)"'
                exec(x)
                for lines in range(len(predictionlist)):
                    x=f'{Ys}={crypt_name}_cbody+f"{arg[lines]} days (predicted) price:  {predictionlist[lines]}\n'
                    exec(x)
            if ne:
                wwwd=requests.get(f"https://www.x-rates.com/calculator/?form=USD&amount={prediction}").text
                wwwd=BeautifulSoup(wwwd,'lxml')
                rdq=wwwd.find_all("span",class_="ccOutputRslt")
                rdq=rdq[0].text
                rdq=str(rdq)
                rdq=rdq.replace(" EUR","")
                rdq=rdq.replace(",","")
                rdq=float(rdq)
                prediction=rdq
            predictionlist.append(prediction)
            month = datetime.now().month     
            #sandp=price_pred("sandp","^GSPC")
    async def find_val(self,crypt_names):
        x=f'self.crypt_names_compred=self.{crypt_names}_list'
        exec(x)
        for line in range(len(self.crypt_names_compred)):
            if self.crypt_names_compred[line]==num1 or num2 or num3 or num4 or num5:
                if self.crypt_names_compred[line]==num5:
                   numdict[crypt_names]="num5"
                   self.num5done=True
                if self.crypt_names_compred[line]==num4:
                   numdict[crypt_names]="num4"
                   self.num4done=True
                if self.crypt_names_compred[line]==num3:
                   numdict[crypt_names]="num3"
                   self.num3done=True
                if self.crypt_names_compred[line]==num2:
                   numdict[crypt_names]="num2"
                   self.num2done=True
                if self.crypt_names_compred[line]==num1:
                    numdict[crypt_names]="num1"
                    self.num1done=True

                x=f"self.cryt_e=self.{crypt_names}_predictionn"
                exec(x)
                self.url="ws://publishingapi.herokuapp.com"
                async with websockets.connect(self.url) as ws:
                    self.serverconnection=True
                    gx=str(self.crypt_names_compred[line])
                    await ws.send(gx)
                    try:
                        if self.num1done==True:
                            if self.num2done==True:
                                if self.num3done==True:
                                    if self.num4done==True:
                                        if self.num5done==True:
                                            await ws.send("[DONE]")
                                            await ws.send(f"[LIST] {serbr}")
                    except:
                        continue
                    

stocks=Stock()
url="ws://publishingapi.herokuapp.com"
async def lsq():
    async with websockets.connect(url) as ws:
        while True:
            print("checking...") 
            ms=await ws.recv()
            print(ms)
            if ms=="[START]":
                print("DONEIWAOFNWIAOBGYHERISNGUESIGNSUISEGINUSEGNUI")
                break
asyncio.run(lsq())
for line in range(len(tr)):
    #print(tr)
    ere=f'e{line}_trplace=str(tr[{line}]).replace("[","").replace("]","").split("href=")'
    exec(ere)
    ewae=f"print(e{line}_trplace)"
    exec(ewae)
    x=f"x=e{line}_trplace[1]"
    exec(x)
    x=x.replace('"','')
    x=x.split(">")
    x=x[0]
    x=x.split("/")
    ere=f'e{line}_trplace=x'
    exec(ere)
    ere=f'e{line}_trplace=e{line}_trplace[3]'
    exec(ere)
    ere=f"e{line}_4lettercode=str(tr[{line}]).split('>')"
    exec(ere)
    ere=f"e{line}_4lettercode=e{line}_4lettercode[1]"
    exec(ere)
    x=f"x=str(e{line}_4lettercode)"
    exec(x)
    x=x.replace("\n","").replace("</a","")
    ere=f"e{line}_4lettercode=x"
    exec(ere)
    ere=f"yx=e{line}_trplace"
    exec(ere)
    stocks.price_pred(yx,x,90)

try:
    num1=min(comparevals)
    print(num1)
    print(comparevals)
    comwda=comparevals
    comwda.remove(num1)
    num2=min(comparevals)
    comwda.remove(num2)
    num3=min(comparevals)
    comwda.remove(num3)
    num4=min(comparevals)
    comwda.remove(num4)
    num5=min(comparevals)
    comwda.remove(num5)
except Exception as e:
    print(e)

for crypto_name in allcryptolist:
    asyncio.run(stocks.find_val(crypto_name))
input()
