import requests
from bs4 import BeautifulSoup

URL = 'https://m.mashina.kg/'

HEADERS = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8',
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0'
}

def get_html(url, params=''):
    request = requests.get(url,headers=HEADERS,params=params)
    return request

def get_data(html):
    bs = BeautifulSoup(html, features='html.parser')
    items = bs.find_all('div',class_='list-item list-label')
    mashina_list = []
    for item in items:
        title = item.find('div',class_='block title').get_text(strip=True)
        price = item.find('div',class_='block price').get_text(strip=True)
        block_counter = item.find('div',class_='block info-wrapper item-info-wrapper').get_text(strip=True)
        city = item.find('div',class_='block city').get_text(strip=True)
        mashina_list.append({'title':title,
                             'price':price,
                             'block_counter':block_counter,
                             'city':city,})
    return mashina_list

def parsing_mashina():
    responce = get_html(URL)
    if responce.status_code == 200:
        mashina_list2=[]
        for page in range(1,2):
            responce = get_html("https://m.mashina.kg/search/all/?region=all",params={'page':page})
            mashina_list2.extend(get_data(responce.text))
        return mashina_list2
    else:
        raise Exception('Error in parsing mashina.kg')
    

