#encoding: utf-8
from scrapy import cmdline


#第一种启动爬虫项目方式i
cmdline.execute(["scrapy",'crawl','qsbk_scrapy'])
#第二种
#mdline.execute("scrapy crawl test_scrapy".split())