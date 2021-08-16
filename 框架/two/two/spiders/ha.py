import scrapy


class HaSpider(scrapy.Spider):
    name = 'ha'
    #allowed_domains = ['www.xxx.com']
    # start_urls = ['https://www.wahaotu.com/meinv/']
    start_urls =['http://www.baidu.com/s?wd=ip']
    # url='https://www.wahaotu.com/meinv/list_%d.html'
    # page=2
    # url='https://www.baidu.com/s?wd=ip'
    def parse(self, response):
        text=response.text
        with open('./1.html','w',encoding='utf-8') as a:
            a.write(text)
        # li_list=response.xpath('/html/body/div[2]/ul/li')
        # for li in li_list:
        #     h=li.xpath('./span/a/span/img/@src')
        #     print(h)
        # if self.page<=5:
        #     newurl=format(self.url%self.page)
        #     self.page+=1
        #     yield scrapy.Request(url=newurl,callback=self.parse)