import requests,os
from bs4 import BeautifulSoup
from urllib.request import urlopen

url="http://news.xinhuanet.com/politics/19cpcnc/2017-10/18/c_1121820173.htm"
html=requests.get(url).text
sp=BeautifulSoup(html,'html.parser')
all_links=sp.find_all(['a','img'])

for link in all_links:
    src=link.get('src')
    href=link.get('href')
    targets=[src,href]

    for t in targets:
        if t!=None and ('.jpg' in t or '.png' in t):
            full_path=t
            print(full_path)
            image_dir='D://images'
            if not os.path.exists(image_dir):
                os.mkdir(image_dir)
            filename=full_path.split('/')[-1]
            image=urlopen(full_path)
            fp=open(os.path.join(image_dir,filename),'wb')
            fp.write(image.read())
            fp.close()