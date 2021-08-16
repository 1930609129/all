import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy_redis.spiders import RedisCrawlSpider
from fbsPro.items import FbsproItem

class FbsSpider(RedisCrawlSpider):
    name = 'fbs'
    # allowed_domains = ['www.x.com']
    # start_urls = ['http://www.x.com/']
    redis_key='sun'
    rules = (
        Rule(LinkExtractor(allow=r'id=1&page=\d+'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        li_lst = response.xpath('/html/body/div[2]/div[3]/ul[2]/li')
        for li in li_lst:
            id = li.xpath('./span[1]/text()').extract_first()
            title = li.xpath('./span[3]/a/text()').extract_first()
            item=FbsproItem()
            item['id']=id
            item['title']=title
            yield item

