# coding=utf-8
import urllib.request
# 3之前的版本直接用urllib即可，下同 #该模块提供了web页面读取数据的接口，使得我们可以像读取本地文件一样读取www或者ftp上的数据
import re
import os

def getHtml(url):
    page = urllib.request.urlopen(url);
    html = page.read();
    return html;


def getImg(html):
    imglist = re.findall('img src="(http.*?)"',html)
    # 1 #http.*?表示非贪婪模式的匹配，只要符合http就匹配完成，不再看后面的内容是否匹配，即在能使整个匹配成功的前提下，使用最少的重复
    return imglist


html = getHtml("https://www.zhihu.com/question/36132174").decode("utf-8");
imagesUrl = getImg(html);

if os.path.exists("E:/imags") == False:
    os.mkdir("E:/imags");

count = 0;  # 文件的起始名称为 0
for url in imagesUrl:
    print(url)
    if (url.find('.') != -1):  # 2
        name = url[url.find('.', len(url) - 5):];
        bytes = urllib.request.urlopen(url);
        f = open("E:/imags/" + str(count) + name, 'wb');  # 代开一个文件，准备以二进制写入文件
        f.write(bytes.read());  # write并不是直接将数据写入文件，而是先写入内存中特定的缓冲区
        f.flush();  # 将缓冲区的数据立即写入缓冲区，并清空缓冲区
        f.close();  # 关闭文件
        count += 1;