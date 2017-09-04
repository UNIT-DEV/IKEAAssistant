# coding:utf-8
'''
Created on 2017年3月7日

@author: liucaiquan
'''
import requests
import json
from wechat import common_params

class Turing(object):
    '''
    classdocs
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
        data = {self.key: self.key_value, self.info: params}

        rsp_dict={}
        rsp_dict[common_params.key_message_type]=common_params.val_msg_type_text
        rsp_dict[common_params.key_content]=requests.post(self.url, data=json.dumps(data)).text

        return rsp_dict
