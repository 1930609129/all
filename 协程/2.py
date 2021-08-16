# -*- coding:utf-8 -*-
import asyncio
import time
async def a(url):
    print("下载",url)
    await asyncio.sleep(2)
    print("完成",url)
start=time.time()
url=['www.baidu.com','www.taoba.com','www.jd.com']
stask=[]
for i in url:
    c=a(i)
    task=asyncio.ensure_future(c)
    stask.append(task)
loop=asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(stask))
print(time.time()-start)