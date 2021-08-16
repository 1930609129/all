import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from redis import Redis
from fbsPro.items import FbsproItem
class FbsSpider(CrawlSpider):
    name = 'fbs'
    conn=Redis(host='127.0.0.1',port=6379)
    # allowed_domains = ['www.x.com']
    start_urls = ['https://www.4567tv.tv/index.php/vod/show/class/%E5%96%9C%E5%89%A7/id/6.html']

    rules = (
        Rule(LinkExtractor(allow=r'/id/6/page/\d+\.html'), callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        li_list=response.xpath('/html/body/div[1]/div/div/div/div[2]/ul/li')
        for li in li_list:
            name=li.xpath('./div/div/h4/a/text()').extract_first()
            url='https://www.4567tv.tv'+li.xpath('./div/div/h4/a/@href').extract_first()
            ex=self.conn.sadd('url',url)
            if ex:
                print('有新数据可爬...')
                item=FbsproItem()
                item['name']=name
                yield scrapy.Request(url=url,callback=self.parse_detail,meta={'item':item})
            else:
                print('该数据已经爬取过了')
    def parse_detail(self,response):
        content=response.xpath('/html/body/div[1]/div/div/div/div[2]/p[5]/span[2]/text()').extract_first()
        # content=str(content)
        item=response.meta['item']
        item['content']=content
        yield item
