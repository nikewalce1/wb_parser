import requests
from bs4 import BeautifulSoup
import json

URL = 'https://wbcon.ru/logistics-kvv/'
HEADERS = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36',
           'accept':'*/*'}
#'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'

def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS,params=params)
    return  r

def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')  # формируются объекты
    #table = soup.find_all('table', class_='result-table')
    td = soup.find_all('td')

    percent = []
    count = 0
    for i in range(len(td)):
        if i == count:
            count += 7
            percent.append({
                'category': td[i].get_text(),
                'subject': td[i+1].get_text(),
                'percent': td[i+2].get_text(),
                'logistics_cost': td[i+3].get_text(),
                'storage_cost': td[i+4].get_text(),
                'delivery_storage_in_liters': td[i + 5].get_text(),
                'paid_acceptance_of_Koledino': td[i + 6].get_text()
            })
    data = json.dumps(percent, ensure_ascii=False)
    #load = json.loads(data)
    #print(load)
    with open("logistics-kvv.json","w", encoding='utf-8') as file:
        file.write(data)



def parse():
    html = get_html(URL)
    if html.status_code == 200:
        get_content(html.text)
    else:
        print('Error')
parse()
