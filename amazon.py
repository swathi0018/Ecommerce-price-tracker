import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = "https://www.amazon.in/Test-Exclusive_2020_1153-Multi-3GB-Storage/dp/B089MSK43J/ref=sr_1_2?crid=1R0OQNSOXR3RY&dchild=1&keywords=redmi+note+10+pro%2B&qid=1623849161&sprefix=redm%2Caps%2C401&sr=8-2"
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Brave Chrome/91.0.4472.101 Safari/537.36'}

def check_price():
    page = requests.get(URL,headers=headers)
    soup=BeautifulSoup(page.content,'html.parser')
    title = soup.find(id='productTitle').get_text()

    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = float(price[2:4]+price[5:8])

    if(converted_price<=17500):
        send_mail()
        
    print(converted_price)
    print(title.strip())

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('swathi.is18@bmsce.ac.in','bcmmkmqhcsijhohu')

    subject = 'Price fell down!'
    body = 'Check the amazon link https://www.amazon.in/Test-Exclusive_2020_1153-Multi-3GB-Storage/dp/B089MSK43J/ref=sr_1_2?crid=1R0OQNSOXR3RY&dchild=1&keywords=redmi+note+10+pro%2B&qid=1623849161&sprefix=redm%2Caps%2C401&sr=8-2'
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
    check_price()
    time.sleep(60)