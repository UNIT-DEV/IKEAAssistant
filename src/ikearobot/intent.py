# coding:utf-8
'''
Created on 2017/9/3 下午2:05

@author: liucaiquan
'''
import json
from baiduunit import baidu_unit_params
from database import database_params


class Intent(object):
    '''
        百度UNIT返回结果解析
    '''

    def __init__(self, query):
        json_object = json.loads(query)
        result = json_object['result']
        schema = result['schema']
        print '百度UNIT解析结果：'
        # 置信度
        self.intent_confidence = schema['intent_confidence']
        print '置信度=' + str(self.intent_confidence)
        # 意图
        self.current_qu_intent = schema['current_qu_intent']
        print '意图=' + str(self.current_qu_intent)
        # 词槽
        bot_merged_slots = schema['bot_merged_slots']
        self.slots = {}
        if bot_merged_slots:
            print 'bot_merged_slots= ' + str(bot_merged_slots)
            for bot_slot in bot_merged_slots:
                self.slots[bot_slot['type']] = bot_slot['original_word']
                print '词槽=' + str(self.slots[bot_slot['type']])
        else:
            print '词槽= 空'

    def get_intent_confidence(self):
        '''
            获取意图置信度
                返回值：浮点类型
        '''
        return self.intent_confidence

    def get_intent(self):
        '''
            获取意图：
                返回值：意图字符串
        '''
        return self.current_qu_intent

    def get_slot_location(self):
        '''
            获取位置的词槽：
                返回值：location 的索引值（整型）
        '''
        if (self.slots.has_key(baidu_unit_params.slot_user_department)):
            return self.slots[baidu_unit_params.slot_user_department]
        elif (self.slots.has_key(baidu_unit_params.slot_user_intent)):
            return self.slots[baidu_unit_params.slot_user_intent]
        else:
            return None

    def get_slot_goods_name(self):
        '''
            获取商品名的词槽
                返回值：商品名
        '''
        if (self.slots.has_key(baidu_unit_params.slot_user_goods)):
            return self.slots[baidu_unit_params.slot_user_goods]
        else:
            return None

    def get_slot_goods_filter(self):
        '''
            获取商品的过滤条件
                返回值：过滤条件
        '''
        if (self.slots.has_key(baidu_unit_params.slot_user_cheap)):
            return database_params.goods_cheap, self.slots[baidu_unit_params.slot_user_cheap]
        elif (self.slots.has_key(baidu_unit_params.slot_user_discount)):
            return database_params.goods_discount, self.slots[baidu_unit_params.slot_user_discount]
        elif (self.slots.has_key(baidu_unit_params.slot_user_new)):
            return database_params.goods_newest, self.slots[baidu_unit_params.slot_user_new]
        else:
            return '', ''
