from urllib import request

import jieba,requests,operator
from bs4 import BeautifulSoup as bs

url="https://movie.douban.com/nowplaying/hangzhou/"

resp = request.urlopen(url)
html_data = resp.read().decode('utf-8')
soup = bs(html_data, 'html.parser')
nowplaying_movie = soup.find_all('div', class_='mod-bd')
nowplaying_movie_list = nowplaying_movie[0].find_all('li', class_='list-item')
nowplaying_list = []
for item in nowplaying_movie_list:
    nowplaying_dict = {}
    nowplaying_dict['id'] = item['data-subject']
    nowplaying_dict['name'] = item['data-title']
    nowplaying_list.append(nowplaying_dict)

print(nowplaying_list)