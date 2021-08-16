import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from sun.items import SunItem,DetailItem

class SuSpider(CrawlSpider):

    name = 'su'
    # allowed_domains = ['www.x.com']
    start_urls = ['https://wz.sun0769.com/political/index/politicsNewest?id=1&page=']
    link_detail=LinkExtractor(allow=r'/political/politics/index\?id=\d+')
    rules = (
        Rule(LinkExtractor(allow=r'id=1&page=\d+'), callback='parse_item', follow=False),
        Rule(link_detail,callback='parse_detail')
    )

    def parse_item(self, response):
        li_lst=response.xpath('/html/body/div[2]/div[3]/ul[2]/li')
        for li in li_lst:
            id=li.xpath('./span[1]/text()').extract_first()
            title=li.xpath('./span[3]/a/text()').extract_first()
            item=SunItem()
            item['id']=id
            item['title']=title
            yield item

    def parse_detail(self,response):

        id=response.xpath('/html/body/div[3]/div[2]/div[2]/div[1]/span[1]/text()').extract_first()
        content=response.xpath('/html/body/div[3]/div[2]/div[2]/div[2]/pre/text()').extract_first()
        item=DetailItem()
        item['id']=id
        item['content']=content
        yield item















    # start_urls = ['http://wz.sun0769.com/political/index/politicsNewest?id=1&page=']
    # # 实例化连接提取器对象
    # # 作用：根据指定的规则 allow=正则表达式 进行指定连接提取
    # link = LinkExtractor(allow=r'id=1&page=\d+')
    # # 获取详情页链接
    # link_detail = LinkExtractor(allow=r'/political/politics/index\?id=\d+')
    # rules = (
    #     # 将link作用到Rule构造方法参数1中
    #     # 作用：将连接提取器提取到的连接进行请求发送并且根据指定规则对请求到的数据进行数据解析
    #     Rule(link, callback='parse_item', follow=False),
    #     # follow=True：将链接提取器  继续作用到  链接提取器提取到的  链接  所对应的  页面中
    #     Rule(link_detail, callback='parse_detail'),
    # )
    #
    # def parse_item(self, response):
    #     li_list = response.xpath('/html/body/div[2]/div[3]/ul[2]/li')
    #     for li in li_list:
    #         id = li.xpath('./span[1]/text()').extract_first()
    #         title = li.xpath('./span[3]/a/text()').extract_first()
    #         item = SunItem()
    #         item['id'] = id
    #         item['title'] = title
    #         yield item
    #
    # def parse_detail(self, response):
    #     content = response.xpath('/html/body/div[3]/div[2]/div[2]/div[2]/pre/text()').extract_first()
    #     id = response.xpath('/html/body/div[3]/div[2]/div[2]/div[1]/span[4]/text()').extract_first()
    #     item = DetailItem()
    #     item['content'] = content
    #     item['id'] = id
    #     yield item
