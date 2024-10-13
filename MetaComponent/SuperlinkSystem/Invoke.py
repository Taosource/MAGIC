# 该模块用于发起链路请求
# 该模块是基于socket的进一步封装

import socket
# 导入socket，提供底层通讯支持
import json
# 导入json数据解析库，为数据解析提供支持


default_settings = {
    "socket_setting" : {
        "ip" : "127.0.0.1",
        "port" : "6789",
        "buffer_size" : 2048,
        "socket_time_out" : 60
    }
}

# 设定一些默认设置，用于离线运行，和初始化时的运行


class CoordinationService():
    """该类是同步服务的一个最小实现，它将出现在所有的元模块中，
    提供解析接收到的数据，得到具体的配置信息，得到的信息将会被传递给
    个个需要加载参数才能启动的模块，比如socket的报文大小的设置,
    同时在不同的模块中，该类将有相同的数据解析实现，和不同的数据传出服务
    通过该操作，所有的模块将遵守相同，或协调的配置进行运行"""
    
    def __init__(self, hand_info: str):
        '''初始化'''
        
        self.hand_info = hand_info
        
        
    def hand_info_exchange(self) -> dict:
        '''用于转换得到的初始信息，将得到的字符串转换为字典，
        并在此过程中处理可能遇到的错误。
        注意：该函数将会返回一个字典，该字典的机构为
        {"hand_data":  ,该键的值是转换后的数据,如果失败则为None
         "data_state":  ,该键的值只有两种状态，T或F，代表数据是否转换成功
         "add_info":  ,该键的值是字典，它是对该数据状态信息的追加，其内部包含两个键，
         分别是{
             "data_type":  ,该键的值有两种T或F，表明的是该数据的类型是否正确
             "exchange":  ，该键的值有三种，分别是F，T和None，分别表示，转换失败，成功，还未转换
         }
            }'''
        
        if type(self.hand_info) == str:
            # 验证得到的信息是否是字符串
            
            out_info = {}
            
            try:
                out_info["hand_data"] = dict(self.hand_info)
                # 尝试进行转换，得到结果
                
                out_info["data_state"] = True
                out_info["add_info"] = {
                    "data_type" : True,
                    "exchange": True
                }
                # 如果转换成功，上述代码将会执行，为附加信息设置正确的值
                
            except:
                out_info["hand_data"] = None
                out_info["data_state"] = False
                out_info["add_info"] =  {
                        "data_type" : True,
                        "exchange" : False
                    }
                
                # 如果转换过程失败，则为附加信息赋予相应的值
                
            finally:
                return out_info
                # 无论是否成功都将结果返回
        
        else:
            # 如果不是字符串则直接返回规定格式的错误结果
            
            return {
                "hand_data" : None,
                "data_state" : False,
                "add_info" : {
                    "data_type" : False,
                    "exchange" : None
                }
            }
                
    
    def hand_info_decrypt(self) -> dict:
        '''用于解密转换后的信息，是否解密及怎么解密，根据具体情况而定
        注意：具体解密的数据为键值对中，值的信息。'''
        
        pass
    
    
    def coordination_service(self):
        '''该函数用于管控整个模块执行某些预加载动作'''
        
        if (intermediary_value := self.hand_info_exchange()["data_state"]):
            # 判断数据是否转换成功 ,使用海象运算符，首先创建变量且赋值，再比较
            
            
            if intermediary_value["encrypt"]:
                # 判断数据是否加密
                
                self.hand_info = self.hand_info_decrypt()
                # 调用解密模块进行数据解密
            
                
        else:
            # 如果失败，则返回规定格式
            
            pass

        
        
# singleton pattern visual resource



class CustomizationSocket():
    """个性化socket，对socket的进一步封装实现自定义的请求，
    为Invoke提供底层的通信细节。简化设计。
    该模块只需要一个参数instructions_info,
    该参数为字典，它包含了该模块所需的所有参数。
    它由两部分构成，即指令参数，主体参数。
    指令参数即针对该模块运行所需的各种参数，
    主体参数即需要被传输的数据。
    它的格式为{
        "communication_protocols": (注：该值为字符串,通过该值设置所需的通讯协议,值只能为udp(UDP)或tcp(TCP)
        "ip_type": (注：该值为字符串，通过该值设置所需的ip类型，值只能为ipv4或ipv6)
        "hand_data": (注：该值类型为字符串，通过它设置需要发送的数据，若数据为其他类型的，则需要转化为字符串)
        }"""
    
    def __init__(self, instructions_info: dict):
        '''用于初始化'''
        
        self.socket_case = None
        # 为socket实例创建一个空位
        self.instructions_info = instructions_info
        # 绑定指令信息，它提供针对各个模块运行所需的基本信息
    

    
    def tcp_ip_ipv4(self):
        '''该函数用于封装socket中的tcp/ip ipv4通讯'''
        self.socket_case = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        # 创建ipv4的tcp通讯的套接字实例
        self.socket_case.connect()
    
    def udp_ip_ipv4(self):
        '''该函数用于封装socket中的tcp/ip ipv4通讯'''
        self.socket_case = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        # 创建ipv4的udp通讯的套接字实例
    
    def tcp_ip_ipv6(self):
        '''该函数用于封装socket中的tcp/ip ipv6通讯'''
        self.socket_case = socket.socket(socket.AF_INET6,socket.SOCK_STREAM)
        # 创建ipv6的tcp通讯的套接字实例
    
    def udp_ip_ipv6(self):
        '''该函数用于封装socket中的udp/ip ipv6通讯'''
        self.socket_case = socket.socket(socket.AF_INET6,socket.SOCK_DGRAM)
        # 创建ipv6的udp通讯的套接字实例
    
    
    def customization_socket(self):
        '''对外的接口，对该模块的调用只需要在调用该函数时传入指令信息，
        它将会根据指令信息执行相应的行为'''
        
        if self.instructions_info["communication_protocols"] == "tcp" or self.instructions_info["communication_protocols"] == "TCP":
            # 判断是否是tcp协议
            if self.instructions_info["ip_type"] == "ipv4":
                # 判断是否是ipv4
                self.tcp_ip_ipv4()
                # 调用对应的模块
            
            if self.instructions_info["ip_type"] == "ipv6":
                # 判断是否是ipv6
                self.tcp_ip_ipv6()
                # 调用对应模块
            
            else:
                pass
            
        if self.instructions_info["communication_protocols"] == "udp" or self.instructions_info["communication_protocols"] == "UDP":
            # 判断是否是udp协议
            if self.instructions_info["ip_type"] == "ipv4":
                # 判断是否是ipv4
                self.udp_ip_ipv4()
                # 调用对应模块
            
            if self.instructions_info["ip_type"] == "ipv6":
                # 判断是否是ipv6
                self.udp_ip_ipv6()
                
            else:
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