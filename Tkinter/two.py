# -*- coding: utf-8 -*-
"""=================================================
# @Time : 2024-10-20 11:15:42
# @IDE -> Interpreter: PyCharm 2021.3 -> python 3.8.10
# @Path : ./useJupyter/Tkinter/two.py
# @Author : Lenovo
# @Describe : 
================================================="""
import tkinter as tk
import time


class TaskTimer:
    def __init__(self, task_name, duration_minutes):
        self.root = tk.Tk()
        self.root.overrideredirect(True)  # 去掉窗口边框和标题栏
        self.root.geometry("300x100+{0}+{1}".format(100, 100))  # 设置窗口位置和大小
        self.root.attributes('-alpha', 0.95)  # 可选：设置窗口透明度
        self.root.attributes('-topmost', True)  # 窗口始终在最前面

        # 为了能够移动窗口，我们需要绑定鼠标事件
        self.root.bind("<ButtonPress-1>", self.on_press)
        self.root.bind("<B1-Motion>", self.on_drag)

        self.task_name = task_name
        self.duration_seconds = duration_minutes * 60
        self.remaining_time = self.duration_seconds

        self.label_task = tk.Label(self.root, text=self.task_name, font=("Arial", 14), bg='white')
        self.label_task.place(x=10, y=10, width=280)

        self.label_time = tk.Label(self.root, text="", font=("Arial", 24), bg='white')
        self.label_time.place(x=10, y=40, width=280, height=40)

        self.update_clock()
        self.root.mainloop()

    def update_clock(self):
        if self.remaining_time > 0:
            minutes, seconds = divmod(self.remaining_time, 60)
            time_string = f"{minutes:02}:{seconds:02}"
            self.label_time.config(text=time_string)
            self.remaining_time -= 1
            self.root.after(1000, self.update_clock)
        else:
            self.label_time.config(text="Time's Up!")
            # 可选：倒计时结束后关闭窗口或执行其他操作
            # self.root.destroy()  # 关闭窗口
            # 或者你可以在这里添加代码来显示一个消息框或者执行其他任务

    def on_press(self, event):
        # 在按下鼠标左键时记录窗口位置
        self.start_x = event.x
        self.start_y = event.y

    def on_drag(self, event):
        # 计算窗口移动的距离
        delta_x = event.x - self.start_x
        delta_y = event.y - self.start_y
        # 移动窗口
        self.root.geometry(
            f"{self.root.winfo_width()}x{self.root.winfo_height()}+{self.root.winfo_x() + delta_x}+{self.root.winfo_y() + delta_y}")


if __name__ == "__main__":
    task_name = "Write Report"
    duration_minutes = 30  # 设置持续时间（分钟）
    app = TaskTimer(task_name, duration_minutes)