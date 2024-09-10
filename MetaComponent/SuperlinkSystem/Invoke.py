# 该模块用于发起链路请求
# 该模块是基于socket的进一步封装

import socket
# 导入socket，提供底层通讯支持
import json
# 导入json数据解析库，为数据解析提供支持



class CoordinationService():
    """该类是同步服务的一个最小实现，它将出现在所有的元模块中，
    提供解析接收到的数据，得到具体的配置信息，得到的信息将会被传递给
    个个需要加载参数才能启动的模块，比如socket的报文大小的设置,
    同时在不同的模块中，该类将有相同的数据解析实现，和不同的数据传出服务
    通过该操作，所有的模块将遵守相同，或协调的配置进行运行"""
    
    def __init__(self, hand_info: str):
        '''初始化'''
        
        self.hand_info = hand_info





class CustomizationSocket():
    """个性化socket，对socket的进一步封装实现自定义的请求，
    为Invoke提供底层的通信细节。简化设计。"""
    
    def __init__(self):
        '''用于初始化'''
        self.socket_case = socket.socket()
        # 实例化一个socket实例
    

    
    def tcp_ip_ipv4(self):
        '''该函数用于封装socket中的tcp/ip ipv4通讯'''
        pass
    
    def udp_ip_ipv4(self):
        '''该函数用于封装socket中的tcp/ip ipv4通讯'''
        pass
    
    def tcp_ip_ipv6(self):
        '''该函数用于封装socket中的tcp/ip ipv6通讯'''
        pass
    
    def udp_ip_ipv6(self):
        '''该函数用于封装socket中的udp/ip ipv6通讯'''
        pass
    
    
    
        
    




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