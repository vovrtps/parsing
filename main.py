import requests
import csv
from bs4 import BeautifulSoup
import re
import datetime

url = 'https://coinmarketcap.com/ru/'
list_s = []
tim = datetime.datetime.now()
pruning = r'(\d+\D\d+)'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

total_s = soup.find('span', class_='sc-4984dd93-0 sc-aec1c3fa-0 fyTlPK').text
total_capitalization = float(' '.join(re.findall(pruning, total_s)))

table = soup.find('div', class_=('sc-14cb040a-2 hptPYH')).find('tbody').find_all('tr')
for tr in table:
    crypt = tr.find_all('p', class_='sc-4984dd93-0 kKpPOn')
    for i in crypt:
        name = i.text

    current_capitalization = tr.find_all('div', class_='sc-500f568e-0 ejtlWy')
    for i in current_capitalization:
        current_capitalizations = i.text
        # print(clubs)

    current_capital = tr.find_all('span', class_='sc-7bc56c81-0 dCzASk')
    for i in current_capital:
        current_capitals = i.text
        current_capitals_pruning = re.findall(pruning, current_capitals)
        market_percentage = f'{float(''.join(current_capitals_pruning)) * 100 / total_capitalization: .1f}'

        result = [f'{name}  {current_capitalizations}  {market_percentage}%']
        list_s.append(result)

with open('CoinMarketCap.csv', 'a', newline='', encoding='utf-8') as f:
    recorder = csv.writer(f, delimiter=' ')
    recorder.writerow([tim.strftime("%H:%M  %dd.%mm.%yy")])
    recorder.writerow(['Name' ' ' 'MC' ' ' 'MP'])
    recorder.writerows(list_s)
    recorder.writerow('') #для пробела между запросами