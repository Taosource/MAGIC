# 该模块用于发起链路请求
# 该模块是基于socket的进一步封装


class CustomizationSocket():
    """个性化socket，对socket的进一步封装实现自定义的请求，
    为Invoke提供底层的通信细节。简化设计。"""
    
    




class InvokeAPI:
    """该类将实现关于链路请求的所有上层功能，
    该类实现的功能即该模块能够被调用的所有功能。"""

    def __init__(self):
        pass

    def invoke(self):
        print("Invoke API called")
        
    def RegistrationLink(self):
        '''注册链接，任何模块加入系统时的首个操作。
        它接受一些基本信息，且它默认启用一个回调函数，
        该回调函数将启动应用的链路响应模块。同时与将会传出认证信息。'''
        print("成功")