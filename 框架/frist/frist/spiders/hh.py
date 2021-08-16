import scrapy
from frist.items import FristItem

class HhSpider(scrapy.Spider):
    name = 'hh'
    # allowed_domains = ['www.xx.com']
    start_urls = ['https://www.qiushibaike.com/text/']

    # def parse(self, response):
    #     div_list=response.xpath('//div[@class="col1 old-style-col1"]/div')
    #     all_data=[]
    #     for div in div_list:
    #         # t=div.xpath('./div[1]/a[2]/h2/text()')[0].extract()
    #         t = div.xpath('./div[1]/a[2]/h2/text()').extract_first()
    #         a=div.xpath('./a[1]/div/span/text()').extract()
    #         a=''.join(a)
    #         dic={
    #             't':t,
    #             'a':a
    #         }
    #         all_data.append(dic)
    #     return all_data

    def parse(self, response):
        div_list=response.xpath('//div[@class="col1 old-style-col1"]/div')
        for div in div_list:
            # t=div.xpath('./div[1]/a[2]/h2/text()')[0].extract()
            t = div.xpath('./div[1]/a[2]/h2/text()').extract_first()
            a=div.xpath('./a[1]/div/span/text()').extract()
            a=''.join(a)
            item=FristItem()
            item['t']=t
            item['a']=a

            yield item   #将item提交给管道