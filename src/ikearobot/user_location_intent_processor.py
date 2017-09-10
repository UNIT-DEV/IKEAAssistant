# coding:utf-8
'''
Created on 2017/9/9 下午3:18

@author: liucaiquan
'''
from wechat import wechat_msg_params
from database.ikea_database import IkeaDatabase
import ikearobot_params
from html_builder import HtmlBuilder
import global_common_params
from requestprocesor import request_params


class UserLocationProcessor(object):
    def __init__(self):
        self.database = IkeaDatabase()
        self.html_builder = HtmlBuilder()

    def __build_webpage_get_url(self, html_file_name):
        rst = ''
        rst += global_common_params.web_server_url
        rst += '?' + request_params.key_req_get_type + '=' + request_params.val_req_get_type_webpage
        rst += '&' + request_params.key_req_get_html_file_name + '=' + html_file_name

        return rst

    def process(self, intent):
        rsp_dict = {}
        rsp_dict[wechat_msg_params.key_message_type] = wechat_msg_params.val_msg_type_invalid

        location = intent.get_slot_location()

        # slot中没有位置信息
        if location is None:
            return rsp_dict

        index = self.database.find_location(location)

        # 位置信息无效
        if (index <= 0):
            return rsp_dict

        html_file_name = self.html_builder.location_build(ikearobot_params.pic_resource_dict[index])

        # TODO: title, description, pic_url后期需要更新
        rsp_dict[wechat_msg_params.key_message_type] = wechat_msg_params.val_msg_type_news
        rsp_dict[wechat_msg_params.key_msg_content_title] = location + u'位置信息'
        rsp_dict[wechat_msg_params.key_msg_content_description] = u'点击查看详细的位置信息'
        rsp_dict[wechat_msg_params.key_msg_content_pciurl] = ikearobot_params.pic_resource_dict[index]
        rsp_dict[wechat_msg_params.key_msg_content_url] = self.__build_webpage_get_url(html_file_name)
        return rsp_dict
