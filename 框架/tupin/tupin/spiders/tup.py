import scrapy
from tupin.items import TupinItem
class TupSpider(scrapy.Spider):
    name = 'tup'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://sc.chinaz.com/tupian/']

    def parse(self, response):
        div_lst=response.xpath('//*[@id="container"]/div')
        for div in div_lst:
            #  使用伪属性
            src=div.xpath('./div/a/img/@src2').extract_first()
            jpg='https:'+src
            item=TupinItem()
            item['jpg']=jpg
            yield item
