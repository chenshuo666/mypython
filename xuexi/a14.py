import requests
url='http://www.baidu.com'
html=requests.get(url).text.splitlines()
for i in range(1,5):
    print(html[i])