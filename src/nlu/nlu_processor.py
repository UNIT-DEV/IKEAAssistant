# coding:utf-8
'''
Created on 2017年8月30日

@author: liucaiquan

请求处理核心模块：
    通过unit平台进行数据处理，使用turing进行兜底处理
'''
from turing.turing import Turing
from ikearobot.ikea_robot import IkeaRobot
from wechat import common_params

class NluProcessor(object):
    def process(self, request):
        # unit 处理
        rst = self.ikea_robot.request(request)

        if (rst[common_params.key_message_type]==common_params.val_msg_type_invalid):
            # turing兜底
            return self.turing.request(request)
        else:
            return rst

    def __init__(self):
        self.ikea_robot = IkeaRobot()
        self.turing = Turing()
