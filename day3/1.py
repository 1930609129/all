# -*- coding:utf-8 -*-
import asyncio
async def fun():
    print('hh')
    re=await asyncio.sleep(2)
    print('h',re)
asyncio.run(fun())