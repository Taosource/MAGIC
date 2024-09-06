# 该模块是一个基本设置模块
# 它通过初始化时的信息对程序进行基本设置
# 便于引导系统的启动
# 注意高级设置请在数据系统中进行设置
# 高级设置将被写入到数据系统中动态变化

import json



SETTINGS_FILE = r"../info/settings.json"
SETTINGS_INFO = {}

with open(SETTINGS_FILE, "r", encoding="utf-8") as f:
    SETTINGS_INFO = json.load(f)


print(SETTINGS_INFO)