# -*- coding: utf-8 -*-
"""=================================================
# @Time : 2026-07-05 16:22:56
# @IDE -> Interpreter: PyCharm 2021.3 -> python 3.8.10
# @Path : ./useJupyter/tools/__init__.py
# @Author : Lenovo
# @Describe : 
================================================="""

import asyncio

async def async_range(n: int):
    for i in range(n):
        yield i

async def print_numbers():
    async for number in async_range(5):
        print(number)
        await asyncio.sleep(1)  # 模拟耗时操作

# 运行异步生成器
#

if __name__ == '__main__':
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(print_numbers())
    # loop.close()
    asyncio.run(print_numbers())