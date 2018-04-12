def use_proxy(proxy_addr,url1):
    import urllib.request
    proxy=urllib.request.ProxyHandler({'http':proxy_addr})
    opener=urllib.request.build_opener(proxy,urllib.request.HTTPHandler)
    urllib.request.install_opener(opener)
    data=urllib.request.Request(url1)
    data1=urllib.request.urlopen(data).read().decode('utf-8')
    return data1

url="182.244.217.208:8118"
data=use_proxy(url,"http://www.baidu.com")
print(data)