# -*- coding:utf-8 -*-
import asyncio
import aiohttp
import time
start=time.time()
urls=['http://127.0.0.1:5000/h','http://127.0.0.1:5000/hh','http://127.0.0.1:5000/hhh']
stask=[]
async def a(url):
    async with aiohttp.ClientSession() as sess:
        async with await sess.get(url) as text:
            nr=await text.text()
            print(nr)
for url in urls:
    c=a(url)
    task=asyncio.ensure_future(c)
    stask.append(task)
loop=asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(stask))
print(time.time()-start)