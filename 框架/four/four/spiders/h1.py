import scrapy


class H1Spider(scrapy.Spider):
    name = 'h1'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.baidu.com/','https://sogou.com']
    
    def parse(self, response):
        print(response)
