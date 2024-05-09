import requests
from headers import http_request
from bs4 import BeautifulSoup
import lxml
import smtplib
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(dotenv_path=find_dotenv())

def send_mail():
    from_add = os.getenv('FROM_ADD')
    to_add = os.getenv('TO_ADD')
    email = os.getenv('FROM_ADD')
    passs = os.getenv('PASSWORD')
    body = f'{product_name} is now Rs.{price_tag}\n{product_url}'
    with smtplib.SMTP('smtp.gmail.com') as smtp:
        smtp.starttls()
        smtp.login(user=email, password=passs)
        smtp.sendmail(from_addr=from_add, to_addrs=to_add, msg=body)
        
product_url = "https://amazon.in/boAt-Cancelling-Bluetooth-Headphones-Immersive/dp/B09MTRDQB5/ref=sr_1_1_sspa?s=electronics&sr=1-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1"

response = requests.get(url=product_url, headers=http_request)

soup = BeautifulSoup(response.text, 'lxml')

price_tag = soup.find('span', class_='a-price-whole').text.replace('.','')
price = int(price_tag.replace(',',''))
product_name = soup.find('span', id='productTitle', class_='a-size-large product-title-word-break').text.strip()
price_symbol = soup.find('span', class_='a-price-symbol').text

if price < 4000:
    send_mail()

print(product_name)
print(price_symbol)

