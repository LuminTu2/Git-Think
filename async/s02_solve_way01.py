# -*- coding: utf-8 -*-
"""=================================================
# @Time : 2026-07-05 21:58:09
# @IDE -> Interpreter: PyCharm 2021.3 -> python 3.8.10
# @Path : ./useJupyter/async/s02_solve_way01.py
# @Author : Lenovo
# @Describe : 
================================================="""
import time
import asyncio

# 异步任务1
async def task1():
    # await 告诉事件循环此处可以挂起，等待 await 后面的对象执行完毕了再向下执行
    # await 后面的对象需要是一个使用 async def 定义对象
    # time.sleep 需要替换为 async def 定义版本的 sleep 函数
    # await time.sleep(5) # 模拟一个耗时 5 秒的 I/O 操作
    print("task1 开始")
    await asyncio.sleep(5)

    print("task1 结束")
    return 10

# 异步任务2
async def task2():
    print('task2 开始')
    await asyncio.sleep(3)
    print("task2 结束")
    return 20

async def main():
    print("main 开始")
    # 获得事件循环
    event_loop = asyncio.get_running_loop()
    # 手动注册任务
    t1 = event_loop.create_task(task1())
    t2 = event_loop.create_task(task2())

    # 等待 t1 任务执行结束，并且获得 t1 任务的执行结果
    # Task 对象
    print(t2, type(t2))
    result = await t2
    print('result2:', result)
    result = await t1
    print('result1:', result)
    print("main 结束")
    print(t2, type(t2))


if __name__ == '__main__':
    start = time.time()
    # 创建事件循环
    event_loop = asyncio.get_event_loop()
    # 启动事件循环
    event_loop.run_until_complete(main())
    print('总耗时：', time.time() - start)

"""
补充说明
  并发执行逻辑：两个任务同时调度，总耗时约 5 秒（由耗时最长的 task1 决定），对比最开始串行 8 秒的同步代码效率大幅提升。
  关键 API 说明：
    get_running_loop()：在已运行的异步函数内部获取当前事件循环
    create_task()：向事件循环提交后台并发任务
    await：挂起当前协程，等待任务完成并取回返回值
    run_until_complete()：主线程启动循环，执行异步入口函数
"""