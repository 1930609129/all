# -*- coding:utf-8 -*-
import asyncio
import requests
import time
start=time.time()
urls=['http://127.0.0.1:5000/h','http://127.0.0.1:5000/hh','http://127.0.0.1:5000/hhh']
stask=[]
async def a(url):
    print("下载",url)
    http=requests.get(url=url).text
    print('完成',http)
for url in urls:
    c=a(url)
    task=asyncio.ensure_future(c)
    stask.append(task)
loop=asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(stask))
print(time.time()-start)