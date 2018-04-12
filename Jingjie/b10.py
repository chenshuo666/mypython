import urllib.request
url='http://blog.csdn.net/weiwei_pig/article/details/51178226'

header='Mozilla/5.0 (Windows NT 10.0; WOW64; rv:55.0) Gecko/20100101 Firefox/55.0'
opener=urllib.request.Request(url)
opener.add_header('User-Agent',header)
data=urllib.request.urlopen(opener).read()
f=open('r.html','w')
f.write(str(data))
f.close()