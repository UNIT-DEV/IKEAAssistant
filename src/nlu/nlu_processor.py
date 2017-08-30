# coding:utf-8
'''
Created on 2017年8月30日

@author: liucaiquan
'''
from turing.turing import Turing
from ikearobot.ikea_robot import IkeaRobot
import json


class NluProcessor(object):
    def get_intent_confidence(self, query):
        json_object = json.loads(query)
        result = json_object['result']
        schema = result['schema']
        return schema['intent_confidence']

    def process(self, request):
        rst = self.ikea_robot.request(request)

        if (self.get_intent_confidence(rst)<50):
            return self.turing.request(request)
        else:
            return rst

    def __init__(self):
        self.ikea_robot = IkeaRobot()
        self.turing = Turing()
