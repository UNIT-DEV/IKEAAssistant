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
import threading
from nlu.nlu_processor import NluProcessor
from wechat import wechat_msg_params
from wechat.message_utils import MessageUtil
import request_params
import global_common_params


class RequestProcessor(object):
    '''
        请求处理器（接入层）
    '''

    def __get(self, requst):
        req_type = requst.get_argument(request_params.key_req_get_type, default='_ARG_DEFAULT')
        req_html_file_name = requst.get_argument(request_params.key_req_get_html_file_name, default='_ARG_DEFAULT')
        if (req_type == request_params.val_req_get_type_webpage):
            requst.render(global_common_params.project_root_path + '/htmls/' + req_html_file_name)
        else:
            requst.write("this is MyWeChatService!")

    def __post(self, request):
        print request.request.body

        # 微信请求数据解析
        req_dict = self.message_util.parse_xml(request)

        # 获取请求文本（语音会转成文本）
        query = ''
        if (req_dict[wechat_msg_params.key_message_type] == wechat_msg_params.val_msg_type_text):
            query = req_dict[wechat_msg_params.key_content]
        elif (req_dict[wechat_msg_params.key_message_type] == wechat_msg_params.val_msg_type_voice):
            query = req_dict[wechat_msg_params.key_recognition]

        # 微信请求处理(核心处理步骤)
        nul_process_rst = self.nul_processor.process(query)

        nul_process_rst[wechat_msg_params.key_to_user_name] = req_dict[wechat_msg_params.key_from_user_name]
        nul_process_rst[wechat_msg_params.key_from_user_name] = req_dict[wechat_msg_params.key_to_user_name]
        msg_time = long(req_dict[wechat_msg_params.key_create_time])
        print 'before, msg_time= ' + str(msg_time)
        msg_time = msg_time + 3
        print 'after, msg_time= ' + str(msg_time)
        nul_process_rst[wechat_msg_params.key_create_time] = str(msg_time)

        # 微信返回数据封装
        rsp_xml = self.message_util.gen_xml(nul_process_rst)
        rsp_xml = self.html_parser.unescape(rsp_xml)

        print rsp_xml

        request.write(rsp_xml)

    '''
        get请求处理
            req：请求句柄
    '''

    def get_processor(self, req):
        print 'get request body: '
        print req.request.body

        # 'echostr'字段用于微信后台服务的配置绑定
        echo_str = req.get_argument('echostr', default='_ARG_DEFAULT')
        if echo_str.strip() == '_ARG_DEFAULT':
            self.__get(req)
        else:
            req.write(echo_str)

            # global_common_params.thread_cnt_lock.acquire()
            # global_common_params.current_thread_num -= 1
            # global_common_params.thread_cnt_lock.release()

    '''
        post请求处理：
            req：请求句柄
    '''

    def post_processor(self, req):
        self.__post(req)

        # global_common_params.thread_cnt_lock.acquire()
        # global_common_params.current_thread_num -= 1
        # global_common_params.thread_cnt_lock.release()

    def __init__(self):
        self.message_util = MessageUtil()
        self.html_parser = HTMLParser.HTMLParser()
        self.nul_processor = NluProcessor()
