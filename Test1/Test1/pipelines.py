# -*- coding: utf-8 -*-
# 爬虫项目的管道文件，主要用来对items里面的定义的数据进行进一步的加工与处理
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class Test1Pipeline(object):
    def process_item(self, item, spider):
        return item
