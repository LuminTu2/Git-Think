# -*- coding: utf-8 -*-
"""=================================================
# @Time : 2026-07-07 07:43:51
# @IDE -> Interpreter: PyCharm 2021.3 -> python 3.8.10
# @Path : ./useJupyter/async/s04_await_future.py
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
    # 注意下面的代码：sleep 内部会执行 await future，此时任务会切换到任务2去执行
    await asyncio.sleep(3)
    result = await sub_task()
    return result

async def start():
    result = await asyncio.gather(task02(), task01())
    print(result)
    print("finished")


if __name__ == '__main__':
    asyncio.run(start())
"""
执行逻辑说明
    asyncio.gather 并发启动 task01、task02；
    先执行 task01，打印 task01，遇到 await asyncio.sleep(3) 主动让出事件循环；
    事件循环切换执行 task02，打印 task02，task02 直接执行完毕返回 200；
    3 秒睡眠结束，切回 task01，执行 await sub_task()，打印 sub_task；
    两个协程全部完成，gather 收集结果按传入顺序输出 [100, 200]。
"""