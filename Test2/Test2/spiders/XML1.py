# -*- coding: utf-8 -*-
from scrapy.spiders import XMLFeedSpider
import Test2.Test2.items

class Xml1Spider(XMLFeedSpider):
    name = 'XML1'
    allowed_domains = ['sina.com.cn']
    start_urls = ['http://blog.sina.com.cn/rss/1615888477.xml']
    iterator = 'iternodes' # 迭代器，'iternodes'是一个基于正则表达式的高性能迭代器
    itertag = 'rss' #设置开始迭代的节点

    def parse_node(self, response, node):# 在节点与所提供的标签名相符合的时候会被调用

        i = Test2.Test2.items.Test2Item()
        i['title'] = node.xpath("/rss/channel/item/title/text()").extract()
        i['link'] = node.xpath("/rss/channel/item/title/text()").extract()
        i['author'] = node.xpath("/rss/channel/item/author/text()").extract()

        for j in range(len(i['title'])):
            print("第"+str(j+1)+"篇文章")
            print("标题是：")
            print(i['tiltle'][j])
            print("对应的链接是：")
            print(i['link'][j])
            print("作者是：")
            print(i['author'][j])
            print("___________________")
        return i
