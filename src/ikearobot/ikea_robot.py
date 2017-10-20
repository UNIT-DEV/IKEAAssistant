# coding:utf-8
'''
Created on 2017年8月30日

@author: liucaiquan
'''
import logging
from baiduunit.baidu_unit import BaiduUnit
from intent import Intent
import json
from database.ikea_database import IkeaDatabase
from wechat import wechat_msg_params
from user_buy_intent_processor import UserBuyProcessor
from user_location_intent_processor import UserLocationProcessor

import global_common_params

logging.basicConfig(level=global_common_params.LOGGER_LEVEL)


class IkeaRobot(object):
    '''
        IKEA机器人（对应图灵机器人）
    '''

    def __init__(self):
        self.unit = BaiduUnit()
        self.scene_id = 9633
        self.min_confidence = 50
        self.database = IkeaDatabase()
        self.user_buy_processor = UserBuyProcessor()
        self.user_location_processor = UserLocationProcessor()

    def request(self, query):
        '''
            ikea请求处理
                query：http请求句柄
                返回值：结果字典
        '''
        rsp_dict = {}

        unit_rst = self.unit.query_request(self.scene_id, query, "").text
        # print "unit_rst=", unit_rst
        logging.info('unit_rst= {}'.format(unit_rst))

        bot_intent = Intent(unit_rst)
        if (bot_intent.get_intent_confidence() < self.min_confidence):
            # 使用图灵机器人兜底
            rsp_dict[wechat_msg_params.key_message_type] = wechat_msg_params.val_msg_type_invalid
        else:
            query_intent = bot_intent.get_intent()

            if (query_intent == 'USER_LOCATION'):
                return self.user_location_processor.process(bot_intent)
            elif (query_intent == 'USER_BUY'):
                return self.user_buy_processor.process(bot_intent)
            else:
                # 兜底
                rsp_dict[wechat_msg_params.key_message_type] = wechat_msg_params.val_msg_type_invalid

        return rsp_dict
