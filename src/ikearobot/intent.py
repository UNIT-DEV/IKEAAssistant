# coding:utf-8
'''
Created on 2017/9/3 下午2:05

@author: liucaiquan
'''
import json
import logging
import baiduunit.baidu_unit_params as baidu_unit_params
import database.database_params as database_params
import global_common_params

logging.basicConfig(level=global_common_params.LOGGER_LEVEL)


class Intent(object):
    '''
        百度UNIT返回结果解析
    '''

    def __init__(self, query):
        json_object = json.loads(query)
        result = json_object['result']
        schema = result['schema']
        # print '百度UNIT解析结果：'
        logging.info(u'百度UNIT解析结果：')
        # 置信度
        self.intent_confidence = schema['intent_confidence']
        # print '置信度=' + str(self.intent_confidence)
        logging.info(u'置信度= {}'.format(str(self.intent_confidence)))
        # 意图
        self.current_qu_intent = schema['current_qu_intent']
        # print '意图=' + str(self.current_qu_intent)
        logging.info(u'意图= {}'.format(str(self.current_qu_intent)))
        # 词槽
        bot_merged_slots = schema['bot_merged_slots']
        self.slots = {}
        if bot_merged_slots:
            # print 'bot_merged_slots= ' + str(bot_merged_slots)
            logging.info('bot_merged_slots= {}'.format(str(bot_merged_slots)))
            for bot_slot in bot_merged_slots:
                self.slots[bot_slot['type']] = bot_slot['original_word']
                # print '词槽=' + str(self.slots[bot_slot['type']])
                logging.info(u'词槽= {}'.format(str(self.slots[bot_slot['type']])))
        else:
            # print '词槽= 空'
            logging.info(u'词槽= 空')

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
        if (self.slots.has_key(baidu_unit_params.SLOT_USER_DEPARTMENT)):
            return self.slots[baidu_unit_params.SLOT_USER_DEPARTMENT]
        elif (self.slots.has_key(baidu_unit_params.SLOT_USER_INTENT)):
            return self.slots[baidu_unit_params.SLOT_USER_INTENT]
        else:
            return None

    def get_slot_goods_name(self):
        '''
            获取商品名的词槽
                返回值：商品名
        '''
        if (self.slots.has_key(baidu_unit_params.SLOT_USER_GOODS)):
            return self.slots[baidu_unit_params.SLOT_USER_GOODS]
        else:
            return None

    def get_slot_goods_filter(self):
        '''
            获取商品的过滤条件
                返回值：过滤条件
        '''
        if (self.slots.has_key(baidu_unit_params.SLOT_USER_CHEAP)):
            return database_params.GOODS_CHEAP, self.slots[baidu_unit_params.SLOT_USER_CHEAP]
        elif (self.slots.has_key(baidu_unit_params.SLOT_USER_DISCOUNT)):
            return database_params.GOODS_DISCOUNT, self.slots[baidu_unit_params.SLOT_USER_DISCOUNT]
        elif (self.slots.has_key(baidu_unit_params.SLOT_USER_NEW)):
            return database_params.GOODS_NEWEST, self.slots[baidu_unit_params.SLOT_USER_NEW]
        else:
            return '', ''
