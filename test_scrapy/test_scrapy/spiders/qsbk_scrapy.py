# -*- coding: utf-8 -*-
import scrapy
from test_scrapy.items import TestScrapyItem
###用来执行xpath\css
from scrapy.http.response.html import HtmlResponse
###提取出来的数据是
from scrapy.selector.unified import SelectorList
class QsbkScrapySpider(scrapy.Spider):
    name = 'qsbk_scrapy'
    allowed_domains = ['qiushibaike.com']
    start_urls = ['https://www.qiushibaike.com/hot/page/2/']
    base_domain = "https://www.qiushibaike.com"

    def parse(self, response):
        duanzi = response.xpath("//div[@id='content-left']/div")
        for shuju in duanzi:
            ###    strip()删除空白
            author = shuju.xpath(".//h2/text()").get().strip()
            content = shuju.xpath(".//div[@class='content']//text()").getall()
            content = "".join(content).strip()
            item = TestScrapyItem(author=author,content=content)
            ##返回解析数据
            yield item
        next_url = response.xpath("//ul[@class='pagination']//li[last()]/a/@href").get()
        if not next_url:
            return
        else:
            yield scrapy.Request(self.base_domain + next_url,callback=self.parse)

