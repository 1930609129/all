import scrapy
from selenium.webdriver import Chrome
from wangyi.items import WangyiItem
class WangSpider(scrapy.Spider):
    name = 'wang'
    # allowed_domains = ['www.x.com']
    start_urls = ['https://news.163.com/']
    urls=[]
    def __init__(self):
        self.web=Chrome(executable_path='D:\基础\chat\自动化1\chromedriver.exe')
    def parse(self, response):
        li_lis=response.xpath('//*[@id="index2016_wrap"]/div[1]/div[2]/div[2]/div[2]/div[2]/div/ul/li')
        ali=[2,3,5,6]
        for index in ali:
            html=li_lis[index].xpath('./a/@href').extract_first()
            self.urls.append(html)
        for url in self.urls:
            yield scrapy.Request(url,callback=self.parse_url)
    def parse_url(self,response):
        div_list=response.xpath('/html/body/div/div[3]/div[4]/div[1]/div[1]/div/ul/li/div/div')
        for div in div_list:
            title=div.xpath('./div/div[1]/h3/a/text()').extract_first()
            item=WangyiItem()
            item['title']=title

            new_detail_url = div.xpath('./div/div[1]/h3/a/@href').extract_first()
            yield scrapy.Request(url=new_detail_url,callback=self.parse_detail,meta={'item':item})

    def parse_detail(self,response):
        content=response.xpath('//*[@id="content"]/div[2]//text()').extract()
        content=''.join(content)
        item=response.meta['item']
        item['content']=content
        yield item

    def closed(self,spider):
        self.web.quit()


