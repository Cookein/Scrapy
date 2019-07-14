# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
from scrapy.exporters import JsonLinesItemExporter
class TestScrapyPipeline(object):
    ####   wb 以二进制的方式打开文件
    def __init__(self):
        self.fp = open("duanzi.json",'wb')
        self.exporter = JsonLinesItemExporter(self.fp,ensure_ascii=False,encoding='utf-8')

    def open_spider(self,spider):
        print('开始抓取---------------')

####爬虫有数据传过来被调用
    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

    def close_spider(self,spider):
        self.fp.close()
        print("爬取结束--------------")
