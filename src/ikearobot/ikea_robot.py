# coding:utf-8
'''
Created on 2017年8月30日

@author: liucaiquan
'''

from baiduunit.unit import BaiduUnit
from intent import Intent
import json
from database.ikea_database import IkeaDatabase


class IkeaRobot(object):
    def __init__(self):
        self.unit = BaiduUnit()
        self.scene_id = 9633
        self.min_confidence = 50
        self.database = IkeaDatabase()

    def request(self, query):
        unit_rst = self.unit.query_request(self.scene_id, query, "").text
        bot_intent = Intent(unit_rst)
        if (bot_intent.get_intent_confidence() < self.min_confidence):
            return ''
        else:
            # TODO:根据实际的intent和slot搜索出合适的结果(数据来源self.database)
            dic = {}
            dic['intent'] = bot_intent.get_intent()
            dic['confidence'] = bot_intent.get_intent_confidence()
            dic['slot'] = bot_intent.get_slots()
            rst_json = json.dumps(dic, ensure_ascii=False)
            return rst_json
