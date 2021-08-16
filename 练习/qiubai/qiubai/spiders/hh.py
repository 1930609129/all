import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from qiubai.items import QiubaiItem
from redis import Redis
import hashlib
class HhSpider(CrawlSpider):
    name = 'hh'
    # allowed_domains = ['www.x.com']
    start_urls = ['https://www.qiushibaike.com/text/']

    rules = (
        Rule(LinkExtractor(allow=r'/text/page/\d+/'), callback='parse_item', follow=False),
        Rule(LinkExtractor(allow=r'/text/$'), callback='parse_item', follow=False)
    )
    conn=Redis(host='127.0.0.1',port=6379,charset='GBK',decode_responses=True)   # 解决中文乱码
    def parse_item(self, response):
        div_list = response.xpath('//div[@class="col1 old-style-col1"]/div')
        for div in div_list:
            item = QiubaiItem()
            item['title'] = div.xpath('./div[1]/a[2]/h2/text()').extract_first()
            content=div.xpath('./a[1]/div/span//text()').extract()
            item['content']=''.join(content)
            source_id=item['title']+item['content']
            md5=hashlib.md5()
            md5.update(str(source_id).encode('utf-8'))
            source_id=md5.hexdigest()
            ex=self.conn.sadd('id',source_id)
            if ex:
                print('该数据正在爬取')
                yield item
            else:
                print('该数据已经爬取过了')

