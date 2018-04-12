# -*- coding: utf-8 -*-
# 爬虫项目的数据容器文件，主要用来定义我们要获取的数据
# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Test1Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    urlname = scrapy.Field()
    urlkey=scrapy.Field()
    urlcr=scrapy.Field()
    urladdr=scrapy.Field()

