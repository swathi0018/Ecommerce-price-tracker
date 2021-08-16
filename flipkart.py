import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = "https://www.flipkart.com/redmi-note-10-pro-vintage-bronze-64-gb/p/itm04ba1f0aed358?pid=MOBGF47CEGZUZGG8&lid=LSTMOBGF47CEGZUZGG86EBA6P&marketplace=FLIPKART&q=redmi+note+10+pro&store=tyy%2F4io&srno=s_1_1&otracker=search&otracker1=search&fm=organic&iid=75309686-2f5f-416c-aacc-67574ac87177.MOBGF47CEGZUZGG8.SEARCH&ppt=None&ppn=None&ssid=qr35ubgysg0000001623859108704&qH=20ef7d326dcad8f3"
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Brave Chrome/91.0.4472.101 Safari/537.36'}

def check_price():
    page = requests.get(URL,headers=headers)
    soup=BeautifulSoup(page.content,'html.parser')

    div_title = soup.find('span',{"class":'B_NuCI'})
    title = str(div_title.text)

    div_price = soup.find('div',{"class":"_30jeq3 _16Jk6d"})
    price = div_price.text
    converted_price = float(price[1:3]+price[4:])

    if(converted_price<=18000):
        send_mail(title,converted_price)
        pass

    print(title)
    print(converted_price)

def send_mail(title,converted_price):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('swathi.is18@bmsce.ac.in','bcmmkmqhcsijhohu')

    subject = 'Price Alert!!!'
    #body = 'Product Name: '+title+'\nPrice: '+str(converted_price)+'\nCheck the Link: '+ URL
    body = 'Product: '+'\nCheck the link: '+URL
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

check_price()