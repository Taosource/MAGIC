# 该文件用于设置系统启动的一些基本参数
# 该文件并不直接存储参数
# 该文件只是设置基本参数，高级参数将会被存储数据系统中

import json
import os
import sys
import re


# 获取路径，构建目录

# 获取工作位置
work_path = os.path.dirname(__file__)
# 获取模块路径
work_file_path = os.path.abspath(__file__)

# 合成完整的settings.json文件的路径,通过使用rfind（）函数匹配最后一个\的索引，
# 来获取基本目录
setting_file_path = os.path.join(work_file_path[0:work_file_path.rfind("\\")], "settings.json")
# 创建一个字典用于存储读取出的数据
setting_data = {}


# 判断工作位置是否位于模块所在位置
if work_file_path == setting_file_path:
    # 如果两者相同那么为True
    path_state_identical = True
    
else:
    # 不相同则为False
    path_state_identical = False 
    


# 打开文件，进行读写
with open(setting_file_path, "+r", encoding="utf-8") as f:
    setting_data = json.load(f)
    
print(setting_data)


