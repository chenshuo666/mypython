

#6.4 ΢������ʵս
#(1)
import re
import urllib.request
import time
import urllib.error
#ģ��������
headers=("User-Agent","Mozilla/5.0 (Windows NT 10.0; WOW64; rv:55.0) Gecko/20100101 Firefox/55.0")
opener = urllib.request.build_opener()
opener.addheaders = [headers]
#��opener��װΪȫ��
urllib.request.install_opener(opener)
#����һ���б�listurl�洢������ַ�б�
listurl=[]
#�Զ��庯��������Ϊʹ�ô��������
def use_proxy(proxy_addr,url):
    #�����쳣�������
    global urllib
    try:
        import urllib.request
        proxy= urllib.request.ProxyHandler({'http':proxy_addr})  
        opener = urllib.request.build_opener(proxy, urllib.request.HTTPHandler)  
        urllib.request.install_opener(opener)
        data = urllib.request.urlopen(url).read().decode('utf-8')
        return data
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)
        #��ΪURLError�쳣����ʱ10��ִ��
        time.sleep(10)
    except Exception as e:
        print("exception:"+str(e))
        #��ΪException�쳣����ʱ1��ִ��
        time.sleep(1)
#��ȡ������������
def getlisturl(key,pagestart,pageend,proxy):
    try:
        page=pagestart
        #����ؼ���key
        keycode=urllib.request.quote(key)
        #����"&page"
        pagecode=urllib.request.quote("&page")
        #ѭ����ȡ��ҳ����������
        for page in range(pagestart,pageend+1):
            #�ֱ𹹽���ҳ��url���ӣ�ÿ��ѭ������һ��
            url="http://weixin.sogou.com/weixin?type=2&query="+keycode+pagecode+str(page)
            #�ô���������������IP����ɱ����
            data1=use_proxy(proxy,url)
            #��ȡ�������ӵ�������ʽ
            listurlpat='<div class="txt-box">.*?(http://.*?)"'
            #��ȡÿҳ�������������Ӳ���ӵ��б�listurl��
            listurl.append(re.compile(listurlpat,re.S).findall(data1))
        print("����ȡ��"+str(len(listurl))+"ҳ") #���ڵ���
        return listurl
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)
        #��ΪURLError�쳣����ʱ10��ִ��
        time.sleep(10)
    except Exception as e:
        print("exception:"+str(e))
        #��ΪException�쳣����ʱ1��ִ��
        time.sleep(1)
#ͨ���������ӻ�ȡ��Ӧ����
def getcontent(listurl,proxy):
    i=0
    #���ñ����ļ��еĿ�ʼhtml����
    html1='''<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
    <html xmlns="http://www.w3.org/1999/xhtml">
    <head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <title>΢������ҳ��</title>
    </head>
    <body>'''
    fh=open("D:/Python35/myweb/part6/1.html","wb")
    fh.write(html1.encode("utf-8"))
    fh.close()
    #�ٴ���׷��д��ķ�ʽ���ļ�����д���Ӧ��������
    fh=open("D:/Python35/myweb/part6/1.html","ab")
    #��ʱlisturlΪ��ά�б�����listurl[][],��һά�洢����Ϣ���ڼ�ҳ��أ��ڶ�ά��ĸ���ҳ�ڼ��������������
    for i in range(0,len(listurl)):
        for j in range(0,len(listurl[i])):
            try:
                url=listurl[i][j]
                #�������ʵurl����������Թ۲��Ӧ��ַ�Ĺ�ϵ���з������ɼ���ַ����ʵ��ַ����һ��amp
                url=url.replace("amp;","")
                #ʹ�ô���ȥ��ȡ��Ӧ��ַ������
                data=use_proxy(proxy,url)
                #���±���������ʽ
                titlepat="<title>(.*?)</title>"
                #��������������ʽ
                contentpat='id="js_content">(.*?)id="js_sg_bar"'
                #ͨ����Ӧ������ʽ�ҵ����Ⲣ�����б�title
                title=re.compile(titlepat).findall(data)
                #ͨ����Ӧ������ʽ�ҵ����ݲ������б�content
                content=re.compile(contentpat,re.S).findall(data)
                #��ʼ������������
                thistitle="�˴�û�л�ȡ��"
                thiscontent="�˴�û�л�ȡ��"
                #��������б�Ϊ�գ�˵���ҵ��˱��⣬ȡ�б�����Ԫ�أ����˴α��⸳������thistitle
                if(title!=[]):
                    thistitle=title[0]
                if(content!=[]):
                    thiscontent=content[0]
                #�����������ݻ��ܸ�������dataall
                dataall="<p>����Ϊ:"+thistitle+"</p><p>����Ϊ:"+thiscontent+"</p><br>"
                #����ƪ���µı��������ݵ�����Ϣд���Ӧ�ļ�
                fh.write(dataall.encode("utf-8"))
                print("��"+str(i)+"����ҳ��"+str(j)+"�δ���") #���ڵ���
            except urllib.error.URLError as e:
                if hasattr(e,"code"):
                    print(e.code)
                if hasattr(e,"reason"):
                    print(e.reason)
                #��ΪURLError�쳣����ʱ10��ִ��
                time.sleep(10)
            except Exception as e:
                print("exception:"+str(e))
                #��ΪException�쳣����ʱ1��ִ��
                time.sleep(1)
    fh.close()
    #���ò�д�뱾���ļ���html����������ִ���
    html2='''</body>
    </html>
    '''
    fh=open("D:/Python35/myweb/part6/1.html","ab")
    fh.write(html2.encode("utf-8"))
    fh.close()
#���ùؼ���            
key="������"
#���ô�����������ô���������п���ʧЧ��������Ҫ�����µ���Ч���������
proxy="119.6.136.122:80"
#����Ϊgetlisturl()��getcontent()���ò�ͬ�Ĵ�����������˴�û�����ø�������
proxy2=""
#��ʼҳ
pagestart=1
#ץȡ����ҳ
pageend=2
listurl=getlisturl(key,pagestart,pageend,proxy)
getcontent(listurl,proxy)