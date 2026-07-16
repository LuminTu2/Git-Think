# -*- coding: utf-8 -*-
"""=================================================
# @Time : 2026-07-07 07:38:22
# @IDE -> Interpreter: PyCharm 2021.3 -> python 3.8.10
# @Path : ./useJupyter/async/s04_await_coroutine.py
# @Author : Lenovo
# @Describe : 
================================================="""
import asyncio

async def task02():
    print('task02')
    return 200

async def sub_task():
    print('sub_task')
    return 100

async def task01():
    print('task01')
    # 一般情况.下，await后面是是一个协程函数的话，事件循环不会直接切换其的任务去执行
    # 而是继续执行后面的协程函数
    result = await sub_task()
    return result

async def start():
    # 在事件循环中注册两个任务 task01 和 task02
    # 并等待两个任务的执行结果
    result = await asyncio.gather(task01(), task02())
    print(result)

if __name__ == '__main__':
    asyncio.run(start())