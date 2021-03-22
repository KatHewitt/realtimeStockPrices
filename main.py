from bs4 import BeautifulSoup
import requests

url = 'https://ca.finance.yahoo.com/quote/TSLA?p=TSLA&.tsrc=fin-tre-srch'

while True:
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'lxml')
    price = soup.find('span', class_ = 'Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)').text
    print(price)


