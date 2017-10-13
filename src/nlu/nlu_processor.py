# coding:utf-8
'''
Created on 2017年8月30日

@author: liucaiquan

请求处理核心模块：
    通过unit平台进行数据处理，使用turing进行兜底处理
'''
from turing.turing import Turing
from ikearobot.ikea_robot import IkeaRobot
from wechat import wechat_msg_params


class NluProcessor(object):
    '''
        自然语言处理
    '''

    def process(self, request):
        '''
            自然语言处理
                request：请求句柄
                返回值：字典结果
        '''
        request = request.replace('。', '')
        print 'query=', request
        # unit 处理
        rst = self.ikea_robot.request(request)

        if (rst[wechat_msg_params.key_message_type] == wechat_msg_params.val_msg_type_invalid):
            # turing兜底
            return self.turing.request(request)
        else:
            return rst

    def __init__(self):
        self.ikea_robot = IkeaRobot()
        self.turing = Turing()
