from bs4 import BeautifulSoup
import requests

url='http://new.cpc.com.tw/division/mb/oil-more4.aspx'

html=requests.get(url).text
sp=BeautifulSoup(html,'html.parser')
data=sp.find_all('span',{'id':'showtd'})
rows=data[0].find_all('tr')

prices=list()
for row in rows:
    cols=row.find_all('td')
    if len(cols[1].text)>0:
        item=[cols[0].text,cols[1].text,cols[2].text,cols.text]
        prices.append(item)

html_body=''
for p in prices:
    html_body+="<tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>".format(p[0],p[1],p[2],p[3])

fp=open('D:\oile.html','w')
fp.write(html_body)
fp.close()