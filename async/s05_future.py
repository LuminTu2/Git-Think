# -*- coding: utf-8 -*-
"""=================================================
# @Time : 2026-07-07 08:06:24
# @IDE -> Interpreter: PyCharm 2021.3 -> python 3.8.10
# @Path : ./useJupyter/async/s05_future.py
# @Author : Lenovo
# @Describe : 
================================================="""
import builtins
abs()
import asyncio
import time
from concurrent.futures import ThreadPoolExecutor

def thread_task(future):
    time.sleep(5)
    future.set_result(100)

async def sub_task():
    print('sub task 开始')
    # 创建 future 对象
    event_loop = asyncio.get_running_loop()
    future = event_loop.create_future()
    # 创建线程池对象
    executor = ThreadPoolExecutor()
    # 在其他线程执行任务
    event_loop.run_in_executor(executor, thread_task, future)
    # 挂起当前任务，事件循环调度其他任务执行
    result = await future
    # await asyncio.sleep(5)
    print('sub task 结束')
    return result

async def task1():
    print('task1 开始')
    result = await sub_task()
    print('task1 结束')
    return result

async def task2():
    print('task2 开始')
    await asyncio.sleep(1)
    print('task2 结束')
    return 200

async def main():
    result = await asyncio.gather(task1(), task2())
    print(result)

if __name__ == '__main__':
    start = time.time()
    asyncio.run(main())
    print("cast: ", time.time() - start)
"""
代码执行逻辑简述
    task1 内部调用 sub_task，sub_task 通过线程池运行阻塞的 time.sleep(5)，并用 Future 接收线程返回结果；
    task2 使用非阻塞的 asyncio.sleep(1)；
    asyncio.gather 并发执行两个任务：
        task1 进入子任务后会阻塞 5 秒；
        事件循环会切换执行 task2，1 秒后 task2 直接完成；
        等待 5 秒线程任务结束后，task1 才完成；
    最终输出 [100, 200]。
"""