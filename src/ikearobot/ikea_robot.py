# coding:utf-8
'''
Created on 2017年8月30日

@author: liucaiquan
'''

from baiduunit.unit import BaiduUnit
from intent import Intent
import json
from database.ikea_database import IkeaDatabase
from wechat import common_params

class IkeaRobot(object):
    def __init__(self):
        self.unit = BaiduUnit()
        self.scene_id = 9633
        self.min_confidence = 50
        self.database = IkeaDatabase()

    def request(self, query):
        rsp_dict={}

        unit_rst = self.unit.query_request(self.scene_id, query, "").text
        bot_intent = Intent(unit_rst)
        if (bot_intent.get_intent_confidence() < self.min_confidence):
            rsp_dict[common_params.key_message_type] = common_params.val_msg_type_invalid
        else:
            # TODO:根据实际的intent和slot搜索出合适的结果(数据来源self.database)
            dic = {}
            dic['intent'] = bot_intent.get_intent()
            dic['confidence'] = bot_intent.get_intent_confidence()
            dic['slot'] = bot_intent.get_slots()
            rst_json = json.dumps(dic, ensure_ascii=False)

            if(dic['intent']=='USER_LOCATION'):
                rsp_dict[common_params.key_message_type]=common_params.val_msg_type_news
                rsp_dict[common_params.key_msg_content_title]= 'news title'
                rsp_dict[common_params.key_msg_content_description]= 'news description'
                rsp_dict[common_params.key_msg_content_pciurl]= 'http://upload-images.jianshu.io/upload_images/851999-d6829d7687f9e074.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240'
                rsp_dict[common_params.key_msg_content_url]= 'https://www.baidu.com'
            else:
                rsp_dict[common_params.key_message_type] =common_params.val_msg_type_text
                rsp_dict[common_params.key_content]=rst_json

        return rsp_dict
