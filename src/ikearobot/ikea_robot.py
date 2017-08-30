# coding:utf-8
'''
Created on 2017年8月30日

@author: liucaiquan
'''

from baiduunit.unit import BaiduUnit


class IkeaRobot(object):
    def __init__(self):
        self.unit = BaiduUnit()
        self.scene_id = 9633

    def request(self, query):
        rst = ''
        rst = self.unit.query_request(self.scene_id, query, "").text
        return rst
