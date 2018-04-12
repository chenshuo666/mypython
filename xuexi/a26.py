from bs4 import BeautifulSoup
import requests
from datetime import datetime
import json
import re

news_url = 'http://news.sina.com.cn/c/nd/2017-05-08/doc-ifyeycfp9368908.shtml'
web_data = requests.get(news_url)
web_data.encoding = 'utf-8'
soup = BeautifulSoup(web_data.text,'lxml')
title = soup.select('#artibodyTitle')[0].text
print(title)

time = soup.select('.time-source')[0].contents[0].strip()
dt = datetime.strptime(time,'%Y年%m月%d日%H:%M')
print(dt)

source = soup.select('.time-source span span a')[0].text
print(source)

print('\n'.join([p.text.strip() for p in soup.select('#artibody p')[:-1]]))

editor = soup.select('.article-editor')[0].text.lstrip('责任编辑：')
print(editor)

comments = requests.get('http://comment5.news.sina.com.cn/page/info?version=1&format=js&channel=gn&newsid=comos-fyeycfp9368908&group=&compress=0&ie=utf-8&oe=utf-8&page=1&page_size=20')
comments_total = json.loads(comments.text.strip('var data='))
print(comments_total['result']['count']['total'])

news_id = re.search('doc-i(.+).shtml',news_url)
print(news_id.group(1))