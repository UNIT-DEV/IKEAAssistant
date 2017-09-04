# coding:utf-8
'''
Created on 2017年8月19日

@author: liucaiquan

数据接入层：
    解析微信后台请求
    转发微信后台请求（后续添加线程池机制）
    请求结果封装成微信后台规范的数据结果返回给微信后台
'''
import HTMLParser

from nlu.nlu_processor import NluProcessor
from wechat import common_params
from wechat.message_utils import MessageUtil


class RequestProcessor(object):
    '''
    classdocs
    '''

    def get(self, requst):
        requst.write("this is MyWeChatService!")

    def post(self, request):
        print request.request.body

        # 微信请求数据解析
        req_dict = self.message_util.parse_xml(request)

        # 获取请求文本（语音会转成文本）
        query = ''
        if (req_dict[common_params.key_message_type] == common_params.val_msg_type_text):
            query = req_dict[common_params.key_content]
        elif (req_dict[common_params.key_message_type] == common_params.val_msg_type_voice):
            query = req_dict[common_params.key_recognition]

        # 微信请求处理(核心处理步骤)
        nul_process_rst=self.nul_processor.process(query)

        nul_process_rst[common_params.key_to_user_name] = req_dict[common_params.key_from_user_name]
        nul_process_rst[common_params.key_from_user_name] = req_dict[common_params.key_to_user_name]
        msg_time = long(req_dict[common_params.key_create_time])
        print 'before, msg_time= ' + str(msg_time)
        msg_time = msg_time + 3
        print 'after, msg_time= ' + str(msg_time)
        nul_process_rst[common_params.key_create_time] = str(msg_time)

        # 微信返回数据封装
        rsp_xml = self.message_util.gen_xml(nul_process_rst)
        rsp_xml = self.html_parser.unescape(rsp_xml)

        print rsp_xml

        request.write(rsp_xml)

    def __init__(self):
        self.message_util = MessageUtil()
        self.html_parser = HTMLParser.HTMLParser()
        self.nul_processor = NluProcessor()
