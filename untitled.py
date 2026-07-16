import json

import yaml
from pygments.lexers import data
from rich import print as rprint
from rich.json import JSON

if __name__ == '__main__':
    # 安全读取单个文档
    with open('show.yaml', 'r', encoding='gbk') as f:
        data = yaml.safe_load(f)
        # indent=4 表示缩进 4 个空格，ensure_ascii=False 防止中文转义
        print(json.dumps(data, indent=2, ensure_ascii=False, sort_keys=True))
        print(data)
        # print(JSON(str(data)))

from termcolor import colored

# 示例JSON数据
data = {   "name": "程序员晚枫",   "age": 30,   "skills": ["Python", "AI", "自动化办公"],   "is_developer": True}
# 使用rich的JSON方法来输出彩色JSON


rprint(JSON.from_data(data))
def fun(x: int) -> int: return 2


# Rich 有一个 inspect 函数，它可以生成任何 Python 对象（例如 class、instance 或 builtin）的报告。

from rich import inspect
inspect(fun, methods=True, private=True)


if __name__ == '__main__':
    print()





