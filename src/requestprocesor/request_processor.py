# coding:utf-8
'''
Created on 2017年8月19日

@author: liucaiquan

数据接入层：
    解析微信后台请求
    转发微信后台请求（后续添加线程池机制）
    请求结果封装成微信后台规范的数据结果返回给微信后台
'''
import sys
import logging
import HTMLParser
import threading

import wechat.wechat_msg_params as wechat_msg_params
import requestprocesor.request_params as request_params
import global_common_params

from nlu.nlu_processor import NluProcessor
from wechat.message_utils import MessageUtil

reload(sys)
sys.setdefaultencoding('utf8')

logging.basicConfig(level=global_common_params.LOGGER_LEVEL)


class RequestProcessor(object):
    '''
        请求处理器（接入层）
    '''

    def __get(self, params):
        html_file = global_common_params.PROJECT_ROOT_PATH + '/htmls/' + params

        return html_file

    def __post(self, request_body):

        # 微信请求数据解析
        req_dict = self.message_util.parse_xml(request_body)

        # 获取请求文本（语音会转成文本）
        query = ''
        if (req_dict[wechat_msg_params.KEY_MESSAGE_TYPE] == wechat_msg_params.VAL_MSG_TYPE_TEXT):
            query = req_dict[wechat_msg_params.KEY_CONTENT]
        elif (req_dict[wechat_msg_params.KEY_MESSAGE_TYPE] == wechat_msg_params.VAL_MSG_TYPE_VOICE):
            query = req_dict[wechat_msg_params.KEY_RECOGNITION]

        # 微信请求处理(核心处理步骤)
        nul_process_rst = self.nul_processor.process(query)

        nul_process_rst[wechat_msg_params.KEY_TO_USER_NAME] = req_dict[wechat_msg_params.KEY_FROM_USER_NAME]
        nul_process_rst[wechat_msg_params.KEY_FROM_USER_NAME] = req_dict[wechat_msg_params.KEY_TO_USER_NAME]
        msg_time = long(req_dict[wechat_msg_params.KEY_CREATE_TIME])
        msg_time = msg_time + 3
        nul_process_rst[wechat_msg_params.KEY_CREATE_TIME] = str(msg_time)

        # 微信返回数据封装
        rsp_xml = self.message_util.gen_xml(nul_process_rst)
        rsp_xml = self.html_parser.unescape(rsp_xml)

        return rsp_xml

    def get_processor(self, html_file):
        '''
            get请求处理
                req：请求句柄
        '''
        return self.__get(html_file)

    def post_processor(self, request_body):
        '''
            post请求处理：
                request_body：post请求body
        '''
        return self.__post(request_body)

    def __init__(self):
        self.message_util = MessageUtil()
        self.html_parser = HTMLParser.HTMLParser()
        self.nul_processor = NluProcessor()
