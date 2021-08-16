# -*- coding:utf-8 -*-
import asyncio
async def a(url):
    print(url)
    return url
c=a('www.baidu.com')
# loop=asyncio.get_event_loop()
# loop.run_until_complete(c)

# loop=asyncio.get_event_loop()
# task=loop.create_task(c)
# loop.run_until_complete(task)

# loop=asyncio.get_event_loop()
# fut=asyncio.ensure_future(c)
# loop.run_until_complete(fut)

# def h(a):
#     print(a.result())
# loop=asyncio.get_event_loop()
# fut=asyncio.ensure_future(c)
# fut.add_done_callback(h)
# loop.run_until_complete(fut)