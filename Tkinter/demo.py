# -*- coding: utf-8 -*-
"""=================================================
# @Time : 2024-10-19 23:51:45
# @IDE -> Interpreter: PyCharm 2021.3 -> python 3.8.10
# @Path : ./useJupyter/Tkinter/demo.py
# @Author : Lenovo
# @Describe : 
================================================="""
import tkinter as tk
import time


class TaskTimer:
    def __init__(self, root, task_name, duration_minutes):
        self.root = root
        self.root.title("Task Timer")
        self.root.geometry("300x100")
        self.root.resizable(False, False)

        self.task_name = task_name
        self.duration_seconds = duration_minutes * 60
        self.remaining_time = self.duration_seconds

        self.label_task = tk.Label(root, text=f"Task: {self.task_name}", font=("Arial", 14))
        self.label_task.pack(pady=10)

        self.label_time = tk.Label(root, text="", font=("Arial", 20))
        self.label_time.pack(pady=10)

        self.update_clock()

    def update_clock(self):
        if self.remaining_time > 0:
            minutes, seconds = divmod(self.remaining_time, 60)
            time_string = f"{minutes:02}:{seconds:02}"
            self.label_time.config(text=time_string)
            self.remaining_time -= 1
            self.root.after(1000, self.update_clock)
        else:
            self.label_time.config(text="Time's Up!")
            self.root.after(3000, self.root.quit)  # Quit the application after 3 seconds


if __name__ == "__main__":
    root = tk.Tk()
    root.attributes('-toolwindow', True)  # This makes the window without the taskbar icon and minimize/maximize buttons
    root.attributes('-topmost', True)  # Keep the window always on top

    task_name = "Write Report"
    duration_minutes = 30  # Set the duration in minutes

    app = TaskTimer(root, task_name, duration_minutes)

    root.mainloop()