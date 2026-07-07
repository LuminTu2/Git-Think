# -*- coding: utf-8 -*-
"""=================================================
# @Time : 2024-10-17 08:37:28
# @IDE -> Interpreter: PyCharm 2021.3 -> python 3.8.10
# @Path : ./useJupyter//tip.py
# @Author : Lenovo
# @Describe : 
================================================="""
import tkinter as tk
from tkinter import messagebox as msg
import datetime as dt
from PIL import Image, ImageTk
import sys, os

name, date = "暂无", ""
size = 50


# 打包exe后的文件路径
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


# 读取文件中日期
with open(resource_path("data.txt"), "r", encoding="utf-8") as file:
    data = file.read()
    data = data.split()
    # 处理
    if len(data) != 0:
        name = data[0]
        date = data[1]

# 窗口初始化
win = tk.Tk()
win.attributes("-transparentcolor", "#F0F0F0")  # 透明
win.overrideredirect(True)  # 无边框
win.geometry("350x200+150+30")  # 位置：屏幕右上角


# 背景图片
def get_img(filename):
    pic = Image.open(filename).resize((345, 200))
    return ImageTk.PhotoImage(pic)


bg = tk.Canvas(win, width=350, height=200)
img = get_img(resource_path("bg.png"))
bg.create_image(175, 100, image=img)
bg.place(x=175, y=100, anchor="center")

day_frm = None


# 更新内容
def update():
    global day_frm, date, name

    if day_frm != None:
        day_frm.destroy()

    day_frm = tk.Frame(win, bg="lightyellow")
    day_frm.pack(anchor="center", fill="both", padx=15, pady=10)

    # 有日期
    if not date == "":
        # 计算剩余天数
        now = dt.datetime.today()
        tar = dt.datetime.strptime(date, "%Y.%m.%d")
        ans = (tar - now).days + 1
        if ans < 0:
            ans = "已过"
        elif ans == 0:
            ans = "今天!"
        else:
            ans = str(ans)

        if ans == "已过" or ans == "今天!":
            size = 40
        elif len(ans) <= 2:
            size = 60
        elif len(ans) <= 3:
            size = 50
        else:
            size = 40
        tk.Label(day_frm, text=ans, bg="lightyellow", font=("黑体", size), justify="right").pack(side="right", padx=15)

    tk.Label(day_frm, text='\n' + name + '\n\n\n' + date, bg="lightyellow", font=("黑体", 18), justify="left").pack(
        side="left", padx=20, pady=5)


update()


# 编辑
def edit():
    global name, date, day_frm

    edit_win = tk.Frame(win, bg="lightyellow")
    edit_win.place(anchor="center", x=175, y=100, width=320, height=170)
    day_frm.destroy()

    # 取消
    def cancel():
        edit_win.destroy()
        update()

    # 文字
    tk.Label(edit_win, text="名称：", bg="lightyellow", font=("微软雅黑", 12)).grid(row=0, column=0, padx=15, pady=15)
    tk.Label(edit_win, text="日期：", bg="lightyellow", font=("微软雅黑", 12)).grid(row=1, column=0, padx=12, pady=8)

    # 输入框
    entry1 = tk.Entry(edit_win, width="22", font=("等线", 13), highlightcolor="blue")
    entry1.grid(row=0, column=1, columnspan=2, padx=15, pady=15)
    entry2 = tk.Entry(edit_win, width="22", font=("等线", 13))
    entry2.grid(row=1, column=1, columnspan=2, padx=12, pady=8)

    # 输入提示
    tk.Label(edit_win, text="如：2024.10.1", bg="lightyellow", fg="darkgrey", font=("微软雅黑", 10)).grid(row=2, column=1)

    # 确定
    def ok():
        global name, date

        name = entry1.get()
        date = entry2.get()

        # 名称为空
        if name == "":
            msg.showerror(title="错误", message="名称不能为空！")
            return

        # 判断日期是否合法
        nums = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        tmp = date.split('.')
        error = False
        if len(tmp) != 3:
            error = True
        for j, i in enumerate(tmp):
            # 是否数字
            if not i.isdigit():
                error = True
                break
            i = int(i)

            if j == 0:  # 年份
                if i < 2000:
                    error = True
            elif j == 1:  # 月份
                if i <= 0 or i > 12:
                    error = True
            elif j == 2:  # 天
                if (int(tmp[0]) % 4 == 0 and int(tmp[0]) % 100 != 0) or int(tmp[0]) % 400 == 0:
                    nums[2] += 1
                if i <= 0 or i > nums[int(tmp[1])]:
                    error = True
                if (int(tmp[0]) % 4 == 0 and int(tmp[0]) % 100 != 0) or int(tmp[0]) % 400 == 0:
                    nums[2] -= 1
        if error:
            msg.showerror(title="错误", message="请输入正确日期！")
            return

        # 更新文件
        with open(resource_path("data.txt"), "w", encoding="utf-8") as file:
            file.write(name + " " + date)

        edit_win.destroy()
        update()

    # 按钮
    tk.Button(edit_win, text="确定", bd=0, bg="lightyellow", activebackground="lightyellow", command=ok,
              font=("微软雅黑", 12), cursor="hand2", activeforeground="grey").grid(row=3, column=1, padx=10, pady=17)
    tk.Button(edit_win, text="取消", bd=0, bg="lightyellow", activebackground="lightyellow", command=cancel,
              font=("微软雅黑", 12), cursor="hand2", activeforeground="grey").grid(row=3, column=2, padx=10, pady=17)


# 按钮
btn_frm = tk.Frame(win, bg="lightyellow")
btn_frm.pack(side="bottom", anchor="e", after=day_frm, padx=25, pady=10)

# 编辑按钮
add_btn = tk.Button(btn_frm, text="编辑", font=("微软雅黑", 12), command=edit,
                    bd=0, bg="lightyellow", activebackground="lightyellow", cursor="hand2", activeforeground="grey")
add_btn.pack(side="right", anchor="s")


# 关闭按钮
def quit():
    win.destroy()


quit_btn = tk.Button(btn_frm, text="关闭", font=("微软雅黑", 12), command=quit,
                     bd=0, bg="lightyellow", activebackground="lightyellow", cursor="hand2", activeforeground="grey")
quit_btn.pack(side="right", anchor="s")


# 置顶按钮
def top():
    win.wm_attributes("-topmost", True)
    top_btn["command"] = no_top
    top_btn["text"] = "取消置顶"


def no_top():
    win.wm_attributes("-topmost", False)
    top_btn["command"] = top
    top_btn["text"] = "置顶"


top_btn = tk.Button(btn_frm, text="置顶", font=("微软雅黑", 12), command=top,
                    bd=0, bg="lightyellow", activebackground="lightyellow", cursor="hand2", activeforeground="grey")
top_btn.pack(side="right", anchor="s")

win.mainloop()