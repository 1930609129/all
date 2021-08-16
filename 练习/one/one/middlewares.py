# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter



from time import sleep
from scrapy.http import HtmlResponse
class OneDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.


    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.
        # web = spider.web
        # if request.url in spider.urls:
        #     web.get(request.url)
        #     sleep(4)
        #     page_text = web.page_source
        #     new_response = HtmlResponse(url=request.url, body=page_text, encoding='utf-8', request=request)
        #     return new_response
        web = spider.web
        if request.url in spider.urls:
            web.get(request.url)
            sleep(4)
            page_text=web.page_source
            new_response=HtmlResponse(url=request.url,body=page_text,encoding='utf-8',request=request)
            return new_response
        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        else:
            return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

