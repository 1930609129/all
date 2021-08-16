# -*- coding:utf-8 -*-

# import requests
# from lxml import etree
# from bs4 import BeautifulSoup
# import time
# import re
# strat=time.time()
# urls=[]
# head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0'}
# html=[]
# def hh():
#     url = 'https://www.3gbizhi.com/mttag/xiaojiejie/'
#     head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0'}
#     req = requests.get(url=url, headers=head).text
#     beau = BeautifulSoup(req, 'lxml')
#     li_lis = beau.find_all('li')
#     for j in li_lis:
#         http = j.a['href'].endswith('.html')
#         if http:
#             html.append(j.a['href'])
# def https(url):
#     req=requests.get(url=url,headers=head).text
#     tree=etree.HTML(req)
#     http=tree.xpath('//div[@class="picimglist pos"]//li')
#     #获取子http
#     for li in http:
#         h=li.xpath('./a/@href')[0]
#         req1 = requests.get(url=h, headers=head).text
#         fc='<div class="showcontw mtw">.*?<img src="(.*?)" id.*?</div>'
#         lis=re.findall(fc,req1,re.S)[0]
#         urls.append(lis)
#
# hh()
# for i in html:
#     https(i)
# for i in urls:
#     fp = './hhh/' + str(time.time()) + '.jpg'
#     jpg=requests.get(url=i,headers=head).content
#     with open(fp,'wb') as a:
#         a.write(jpg)
# print(time.time()-strat)


# import requests
# from lxml import etree
# from bs4 import BeautifulSoup
# import time
# import re
# start=time.time()
# urls=[]
# head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0'}
# html=[]
# def hh():
#     url = 'https://www.3gbizhi.com/mttag/xiaojiejie/'
#     head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0'}
#     req = requests.get(url=url, headers=head).text
#     beau = BeautifulSoup(req, 'lxml')
#     li_lis = beau.find_all('li')
#     for j in li_lis:
#         http = j.a['href'].endswith('.html')
#         if http:
#             html.append(j.a['href'])
# def https(url):
#     req=requests.get(url=url,headers=head).text
#     tree=etree.HTML(req)
#     http=tree.xpath('//div[@class="picimglist pos"]//li')
#     #获取子http
#     for li in http:
#         h=li.xpath('./a/@href')[0]
#         req1 = requests.get(url=h, headers=head).text
#         fc='<div class="showcontw mtw">.*?<img src="(.*?)" id.*?</div>'
#         lis=re.findall(fc,req1,re.S)[0]
#         urls.append(lis)
#
# hh()
# for i in html:
#     https(i)
#
#
# import asyncio
# import aiohttp
# stark=[]
# async def h(url):
#     async with aiohttp.ClientSession() as sess:
#         async with await sess.get(url,headers=head) as text:
#             nr=await text.read()
#             fp = './hhh/' + str(time.time()) + '.jpg'
#             with open(fp,'wb') as a:
#                 a.write(nr)
# for i in urls:
#     c=h(i)
#     task=asyncio.ensure_future(c)
#     stark.append(task)
# loop=asyncio.get_event_loop()
# loop.run_until_complete(asyncio.wait(stark))
# print(time.time()-start)

# import requests
# from lxml import etree
# from bs4 import BeautifulSoup
# import time
# import re
# import asyncio
# import aiohttp
# start=time.time()
# urls=[]
# head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0'}
# html=[]
# def hh():
#     url = 'https://www.3gbizhi.com/mttag/xiaojiejie/'
#     head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0'}
#     req = requests.get(url=url, headers=head).text
#     beau = BeautifulSoup(req, 'lxml')
#     li_lis = beau.find_all('li')
#     for j in li_lis:
#         http = j.a['href'].endswith('.html')
#         if http:
#             html.append(j.a['href'])
# stask=[]
# async def https(url):
#     async with aiohttp.ClientSession() as sess:
#         async with await sess.get(url, headers=head) as text:
#             nr = await text.text()
#             tree=etree.HTML(nr)
#             http=tree.xpath('//div[@class="picimglist pos"]//li')
#             #获取子http
#             for li in http:
#                 h = li.xpath('./a/@href')[0]
#                 req1 = requests.get(url=h, headers=head).text
#                 fc='<div class="showcontw mtw">.*?<img src="(.*?)" id.*?</div>'
#                 lis=re.findall(fc,req1,re.S)[0]
#                 urls.append(lis)
#
# hh()
# for url in html:
#     c=https(url)
#     task=asyncio.ensure_future(c)
#     stask.append(task)
# loop=asyncio.get_event_loop()
# loop.run_until_complete(asyncio.wait(stask))
# stark=[]
# async def h(url):
#     async with aiohttp.ClientSession() as sess:
#         async with await sess.get(url,headers=head) as text:
#             nr=await text.read()
#             fp = './hhh/' + str(time.time()) + '.jpg'
#             with open(fp,'wb') as a:
#                 a.write(nr)
# for i in urls:
#     c=h(i)
#     task=asyncio.ensure_future(c)
#     stark.append(task)
# loop=asyncio.get_event_loop()
# loop.run_until_complete(asyncio.wait(stark))
#
#
# # stark=[]
# # async def h(url):
# #     async with aiohttp.ClientSession() as sess:
# #         async with await sess.get(url,headers=head) as text:
# #             nr=await text.read()
# #             fp = './hhh/' + str(time.time()) + '.jpg'
# #             with open(fp,'wb') as a:
# #                 a.write(nr)
# # for i in urls:
# #     c=h(i)
# #     task=asyncio.ensure_future(c)
# #     stark.append(task)
# # loop=asyncio.get_event_loop()
# # loop.run_until_complete(asyncio.wait(stark))
# print(time.time()-start)
