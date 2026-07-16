# -*- coding: utf-8 -*-
"""=================================================
# @Time : 2024-09-18 19:44:30
# @IDE -> Interpreter: PyCharm 2021.3 -> python 3.8.10
# @Path : ./useJupyter//handleGif.py
# @Author : Lenovo
# @Describe : 
================================================="""
import os.path

class Renames:
    def __init__(self, directory):
        self.directory = directory

    def displays(self):
        # res = set()
        # if os.path.exists(self.directory):
        #     allfile =
        # else:
        #     return res
        # for root, dirs, files in os.walk(self.directory):
        #     level = root.replace(self.directory, '').count(os.sep)
        #     print(dirs)
        #     indent = ' ' * 4 * (level)
        #     print('{}{}/'.format(indent, os.path.basename(root)))
        #     subindent = ' ' * 4 * (level + 1)
        #     for f in files:
        #         print('{}{}'.format(subindent, f))
        se = []
        for filename in os.listdir(self.directory):
            file_path = os.path.join(self.directory, filename)
            if os.path.isfile(file_path):
                # print(filename)
                se.append(filename)
        return se


    def renamefile(self):
        re = self.displays()
        # print(re)
        res = [os.path.join(self.directory, x) for x in re]
        print(res)

if __name__ == '__main__':
    dire = r'D:\Android\Projects\MyApplication20240918\app\src\main\res\drawable'
    renames = Renames(dire)
    renames.renamefile()