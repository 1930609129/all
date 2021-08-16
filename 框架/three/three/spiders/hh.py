import scrapy

class HhSpider(scrapy.Spider):
    name = 'hh'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.kanxiaojiejie.com/']
    urls = 'https://www.kanxiaojiejie.com/page/%d'
    mun=2
    def parse(self, response):
        lis=response.xpath('//*[@id="masonry"]/article')
        for a in lis:
            src=a.xpath('./div/div/a/img/@src').extract_first()
            print(src)
        if self.mun<=3:
            newurl=format(self.urls%self.mun)
            self.mun+=1
            yield scrapy.Request(url=newurl,callback=self.parse)



