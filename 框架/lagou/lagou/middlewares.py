# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter

import random
from scrapy.http import HtmlResponse
from time import sleep
class LagouDownloaderMiddleware:
    i = -1
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.


    def process_request(self, request, spider):
        # request.headers['User-Agent'] = random.choices(self.user_agent_list)
        # # request.meta['proxy'] = 'http://' + random.choice(self.PROXY_https)
        return None

    def process_response(self, request, response, spider):
        url = 'https://www.lagou.com/zhaopin/Java/'
        conn = spider.conn
        if spider.urls !=[]:
            self.i+=1
            if self.i<=len(spider.urls):
                conn.get(spider.urls[self.i])
                print(spider.urls[self.i])
                page_text = conn.page_source
                new_response = HtmlResponse(url=spider.urls[self.i], body=page_text, encoding='utf-8', request=request)
                sleep(3)
                return new_response
        else:
            conn.get(url)
            sleep(2)
            page_text = conn.page_source
            response = HtmlResponse(url=url, body=page_text, encoding='utf-8', request=request)
            return response

        #
        # if request.url in spider.urls:
        #     conn.get(request.url)
        #     sleep(4)
        #     page_text = conn.page_source
        #     new_response = HtmlResponse(url=request.url, body=page_text, encoding='utf-8', request=request)
        #     return new_response
        # else:
        #     url = 'https://www.lagou.com/zhaopin/Java/'
        # url = 'https://www.lagou.com/jobs/7440901.html?show=e5dfd8936a3246ac8e05d59a409e8fd5'

        # Called with the response returned from the downloader.
        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest

    def process_exception(self, request, exception, spider):
        # if request.url.split(':')[0] == 'http':
        #     request.meta['proxy'] = 'http://' + random.choice(self.PROXY_http)
        # else:
        #     request.meta['proxy'] = 'https://' + random.choice(self.PROXY_https)
        return request
