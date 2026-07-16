# -*- coding: utf-8 -*-
import os
import random


def main():
    fruits = ('草莓', '葡萄', '西瓜')  # 使用复数形式更直观
    style = {fruit: 0 for fruit in fruits}  # 变量名使用小写字母和下划线
    directory = r'.\test'  # 使用更明确的变量名
    if not os.path.exists(directory):
        os.makedirs(directory)

    for _ in range(10):
        fruit = random.choice(fruits)
        style[fruit] += 1
        file_name = f"{fruit}_{style[fruit]:02d}.txt"  # 使用f-string简化字符串格式化
        file_path = os.path.join(directory, file_name)
        try:
            with open(file_path, 'w', encoding='utf-8') as file:
                # 写入一些内容到文件
                file.write(f"这是第{style[fruit]}个{fruit}。\n")
        except Exception as e:
            print(f"写入文件时发生错误：{e}")


if __name__ == '__main__':
    main()
