# -*- coding:utf-8 -*-
# import requests
# from lxml import etree
# url='https://www.qiushibaike.com/text/'
# head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0'}
# text=requests.get(url=url,headers=head).text
# h=etree.HTML(text)
# lis=h.xpath('//div[@class="content"]/span//text()')
# for i in lis:
#     print(i)

# import requests
# from lxml import etree
# url='https://jobs.51job.com/guangzhou-byq/129558910.html?'
# head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0'}
# data={'s': 'sou_sou_soulb',
# 't': '0'}
# text=requests.get(url=url,headers=head,params=data).text.encode('iso-8859-1')
# h=etree.HTML(text)
# lis=h.xpath('//div[@class="bmsg job_msg inbox"]//text()')
# for i in lis:
#     print(i)
