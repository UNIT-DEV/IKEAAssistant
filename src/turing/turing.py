# coding:utf-8
'''
Created on 2017年3月7日

@author: liucaiquan
'''
import requests
import json


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
        return requests.post(self.url, data=json.dumps(data)).text
