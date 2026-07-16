# -*- coding: utf-8 -*-
"""=================================================
# @Time : 2024-09-07 10:43:27
# @IDE -> Interpreter: PyCharm 2021.3 -> python 3.8.10
# @Path : ./useJupyter//handle.py
# @Author : Lenovo
# @Describe : 
================================================="""

if __name__ == '__main__':
    with open(r".\requirements.txt", 'r', encoding='utf-8') as file:
        rows = [row.rstrip() for row in file.readlines()]
        packages = [st.split()[0] + '\n' for st in rows]
        with open(r'.\handle.txt', 'w', encoding='utf-8') as infile:
            infile.writelines(packages)

