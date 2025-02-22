import requests
from bs4 import BeautifulSoup

URL = 'https://rezka.ag/'

HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8',
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0'
}

#1 создания запроса
def get_html(url,params=''):
    request = requests.get(url,headers=HEADERS,params=params)
    return request

#2 получение data
def get_data(html):
    bs = BeautifulSoup(html, features='html.parser')
    items = bs.find_all('div',class_='b-content__inline_item')
    rezka_list = []
    for item in items:
        title = item.find('div',class_='b-content__inline_item-link').get_text(strip=True)
        rezka_list.append({'title':title})
    return rezka_list

#3 start func
def parsing_rezka():
    responce = get_html(URL)
    if responce.status_code == 200:
        rezka_list2 = []
        for page in range(1,2):
            responce = get_html("https://rezka.ag/films/", params={'page':page})
            rezka_list2.extend(get_data(responce.text))
        return rezka_list2
    else:
        raise Exception('Error  in parsing rezka')


        