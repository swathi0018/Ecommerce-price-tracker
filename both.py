import requests
from bs4 import BeautifulSoup
import smtplib
import time

#Amazon Link
URL1 = "https://www.amazon.in/Nokia-3-4-Dusk-64GB-Storage/dp/B08VB2H7NJ/ref=sr_1_1_sspa?dchild=1&keywords=nokia&qid=1623870054&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExSDMwSkJSQUgzQ1M0JmVuY3J5cHRlZElkPUEwMjM3ODg5M0VaTDlIUTZNOVFCVSZlbmNyeXB0ZWRBZElkPUExMDIzODIwMkFQM0JSOVI2NkdHWCZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU="

#Flipkart Link
URL2 = "https://www.flipkart.com/nokia-ta-1010-105/p/itmb460ca8c6c956?pid=MOBEWSZFGGR4QMCE&lid=LSTMOBEWSZFGGR4QMCENO26JU&marketplace=FLIPKART&q=nokia&store=search.flipkart.com&srno=s_1_1&otracker=search&otracker1=search&fm=SEARCH&iid=3a411d33-99bf-4e93-8e4f-c46ab869de66.MOBEWSZFGGR4QMCE.SEARCH&ppt=sp&ppn=sp&ssid=dj83txq5sw0000001623869996986&qH=0c23a8bf29a191f1"
#Set your target price here
budget = 100000

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Brave Chrome/91.0.4472.101 Safari/537.36'}


def check_price_amazon():
    page = requests.get(URL1,headers=headers)
    soup=BeautifulSoup(page.content,'html.parser')
    title = soup.find(id='productTitle').get_text()

    price = soup.find(id="priceblock_ourprice").get_text()
    value = price[2:]
    converted_price = float(value.replace(",",""))

    #print('Amazon Title:'+title.strip())
    #print('Amazon Price:'+str(converted_price))

    return converted_price


def check_price_flipkart():
    page = requests.get(URL2,headers=headers)
    soup=BeautifulSoup(page.content,'html.parser')

    div_title = soup.find('span',{"class":'B_NuCI'})
    title = str(div_title.text)

    div_price = soup.find('div',{"class":"_30jeq3 _16Jk6d"})
    price = div_price.text
    value = price[1:]
    converted_price = float(value.replace(",",""))

    #print('Flipkart Title:'+title)
    #print('Flipkart Price:'+str(converted_price))

    return converted_price
    

def send_mail(URL,website,price):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('swathi.is18@bmsce.ac.in','bcmmkmqhcsijhohu')

    print('Amazon Price:'+str(price))
    print('Flipkart Price:'+str(price))

    subject = 'Price Alert on '+website+"!!!"
    body = 'Price: '+str(price)+'\nCheck the link: '+URL
    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        #from mail address
        'swathi.is18@bmsce.ac.in',
        #to mail address
        'swathiashok555@gmail.com',
        msg
    )
    print('EMAIL HAS BEEN SENT!')

    server.quit()

while(True):

    if check_price_amazon()<check_price_flipkart():
        if check_price_amazon()<=budget: send_mail(URL1,'Amazon',check_price_amazon())
    elif check_price_amazon()>check_price_flipkart():
        if check_price_flipkart()<=budget: send_mail(URL2,'Flipkart',check_price_flipkart())
    else:
        if (check_price_amazon() or check_price_flipkart())<=budget:
            send_mail(URL1,'Amazon',check_price_amazon())
            send_mail(URL2,'Flipkart',check_price_flipkart())

    time.sleep(60*5)
