"""
    程序入口
"""

from ui import *

# 限制只能从当前模块才执行。
if __name__ =="__main__":
    try:
        view = StudentManagerView()
        view.main()
    except:
        print("出错啦")
