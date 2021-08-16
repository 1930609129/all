import scrapy
from selenium.webdriver import Chrome

class LaouSpider(scrapy.Spider):
    name = 'laou'
    # allowed_domains = ['www.x.com'] https://www.lagou.com/zhaopin/Java/
    start_urls = ['https://www.lagou.com/']
    urls = []
    conn=Chrome(executable_path='D:\基础\chat\自动化1\chromedriver.exe')
    def parse(self, response):
        # content = response.xpath('//*[@id="job_detail"]/dd[2]/div//text()').extract()
        # print(content)
        li_lis=response.xpath('//*[@id="s_position_list"]/ul/li')
        for li in li_lis:
            title=li.xpath('./div[1]/div[1]/div[1]/a/h3/text()').extract_first()
            html=li.xpath('./div[1]/div[1]/div[1]/a/@href').extract_first()
            self.urls.append(html)
        for url in self.urls:
            yield scrapy.Request(url=url,callback=self.parse_detail)
    def parse_detail(self,response):
        content=response.xpath('//*[@id="job_detail"]/dd[2]/div//text()').extract()
        content=''.join(content)
        print(content)

    def closed(self,spider):
        self.conn.quit()