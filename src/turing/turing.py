# coding:utf-8
'''
Created on 2017年3月7日

@author: liucaiquan
'''
import requests
import json
from wechat import wechat_msg_params


class Turing(object):
    '''
    图灵接口处理
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.key = "key"
        self.key_value = "5e3c2b7eb5bb42caad216d02cde38920"
        self.info = "info"
        self.url = "http://www.tuling123.com/openapi/api"

    def request(self, params):
        '''
            图灵接口请求
                params：请求字符串
                返回值：字典结果
        '''
        data = {self.key: self.key_value, self.info: params}

        rsp_dict = {}
        rsp_dict[wechat_msg_params.key_message_type] = wechat_msg_params.val_msg_type_text
        turing_request_rst = json.loads(requests.post(self.url, data=json.dumps(data)).text)
        print 'type(turing_request_rst): '
        print type(turing_request_rst)
        rsp_dict[wechat_msg_params.key_content] = turing_request_rst['text']

        return rsp_dict
