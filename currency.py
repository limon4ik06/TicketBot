import requests
from bs4 import BeautifulSoup
class currency():
        def curs_usd(self):
                url = 'https://minfin.com.ua/currency/banks/usd/'
                r = requests.get(url)
                soup = BeautifulSoup(r.text, 'lxml')
                info = soup.find('div', class_='mfm-grey-bg').find('td', class_='responsive-hide mfm-text-left mfm-pl0').text
                return info
