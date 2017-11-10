# coding:utf-8
'''
Created on 2017年8月30日

@author: liucaiquan

请求处理核心模块：
    通过unit平台进行数据处理，使用turing进行兜底处理
'''
import logging
import wechat.wechat_msg_params as wechat_msg_params
import global_common_params

from turing.turing import Turing
from ikearobot.ikea_robot import IkeaRobot

logging.basicConfig(level=global_common_params.LOGGER_LEVEL)


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
        # print 'query=', request
        logging.info('query= {}'.format(request))

        if global_common_params.IKEA_ASSISTANT_SWITCH:
            # unit 处理
            rst = self.ikea_robot.request(request)

            if (rst[wechat_msg_params.KEY_MESSAGE_TYPE] == wechat_msg_params.VAL_MSG_TYPE_INVALID):
                # turing兜底
                return self.turing.request(request)
            else:
                return rst
        else:
            return self.turing.request(request)

    def __init__(self):
        self.ikea_robot = IkeaRobot()
        self.turing = Turing()
