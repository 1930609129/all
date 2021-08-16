import scrapy
from one.items import OneItem

class LagouSpider(scrapy.Spider):
    name = 'lagou'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.kanxiaojiejie.com/']
    def htmlparse(self,response):
        lst=response.xpath('//*[@id="page"]/div/div/div/div[1]/div/article')
        for i in lst:
            jpg=i.xpath('./div/div/a/img/@src').extract_first()
            item=OneItem()
            item['jpg']=jpg
            yield item
            # print(jpg)

    def parse(self, response):
        li_list=response.xpath('//*[@id="masonry"]/article')
        for li in li_list:
            jpg=li.xpath('./div/div/a/img/@src').extract_first()
            # print(jpg)
            item=OneItem()
            item['jpg']=jpg
            yield item
            html=li.xpath('./div/div/a/@href').extract_first()
            yield scrapy.Request(html,callback=self.htmlparse)

