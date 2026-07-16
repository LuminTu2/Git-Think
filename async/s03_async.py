# -*- coding: utf-8 -*-
"""=================================================
# @Time : 2026-07-05 23:31:46
# @IDE -> Interpreter: PyCharm 2021.3 -> python 3.8.10
# @Path : ./useJupyter/async/s03_async.py
# @Author : Lenovo
# @Describe : 
================================================="""
import asyncio


async def hi():
    print("Hello!")
    await asyncio.sleep(5)

if __name__ == '__main__':
    coroutine = hi()
    print(coroutine)
    print(type(hi))
    print(type(coroutine))
    coroutine.close() # asyncio.run(coroutine)