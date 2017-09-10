# coding:utf-8
'''
Created on 2017年8月30日

@author: liucaiquan
'''

from baiduunit.baidu_unit import BaiduUnit
from intent import Intent
import json
from database.ikea_database import IkeaDatabase
from wechat import wechat_msg_params
from user_buy_intent_processor import UserBuyProcessor
from user_location_intent_processor import UserLocationProcessor


class IkeaRobot(object):
    def __init__(self):
        self.unit = BaiduUnit()
        self.scene_id = 9633
        self.min_confidence = 50
        self.database = IkeaDatabase()
        self.user_buy_processor = UserBuyProcessor()
        self.user_location_processor = UserLocationProcessor()

    def request(self, query):
        rsp_dict = {}

        unit_rst = self.unit.query_request(self.scene_id, query, "").text
        bot_intent = Intent(unit_rst)
        if (bot_intent.get_intent_confidence() < self.min_confidence):
            # 使用图灵机器人兜底
            rsp_dict[wechat_msg_params.key_message_type] = wechat_msg_params.val_msg_type_invalid
        else:
            query_intent = bot_intent.get_intent()

            if (query_intent == 'USER_LOCATION'):
                # # 临时测试，后期直接删除
                # rsp_dict[wechat_msg_params.key_message_type]=wechat_msg_params.val_msg_type_news
                # rsp_dict[wechat_msg_params.key_msg_content_title]= 'title'
                # rsp_dict[wechat_msg_params.key_msg_content_description]= 'description'
                # rsp_dict[wechat_msg_params.key_msg_content_pciurl]= 'http://upload-images.jianshu.io/upload_images/4905018-b72bb56e2ac68048.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240'
                # rsp_dict[wechat_msg_params.key_msg_content_url]= 'http://120.25.220.14?req_get_type=webpage'

                # TODO:根据实际的intent和slot搜索出合适的结果(数据来源self.database)
                return self.user_location_processor.process(bot_intent)
            elif (query_intent == 'USER_BUY'):
                # # 临时测试，后续直接删除
                # rsp_dict[wechat_msg_params.key_message_type] =wechat_msg_params.val_msg_type_text
                # rsp_dict[wechat_msg_pa˙rams.key_content]=rst_json
                #
                # rsp_dict=self.user_buy_processor.process(query_dic)

                return self.user_buy_processor.process(bot_intent)
            else:
                # 兜底
                rsp_dict[wechat_msg_params.key_message_type] = wechat_msg_params.val_msg_type_invalid

        return rsp_dict
