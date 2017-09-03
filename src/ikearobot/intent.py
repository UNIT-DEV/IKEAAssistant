# coding:utf-8
'''
Created on 2017/9/3 下午2:05

@author: liucaiquan
'''
import json
class Intent(object):
    pass

    def __init__(self, query):
        json_object = json.loads(query)
        result = json_object['result']
        schema = result['schema']
        # 置信度
        self.intent_confidence= schema['intent_confidence']
        # 意图
        self.current_qu_intent=schema['current_qu_intent']
        bot_merged_slots=schema['bot_merged_slots']
        # 词槽
        self.slots={}
        for bot_slot in bot_merged_slots:
            self.slots[bot_slot['type']]=bot_slot['original_word']

    # 置信度
    def get_intent_confidence(self):
        return  self.intent_confidence

    # 意图
    def get_intent(self):
        return self.current_qu_intent

    # 词槽
    def get_slots(self):
        return self.slots
