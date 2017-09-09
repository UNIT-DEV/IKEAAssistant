#coding:utf-8
'''
Created on 2017/9/9 下午3:19

@author: liucaiquan
'''
from html_builder import HtmlBuilder
from wechat import wechat_msg_params
from database.ikea_database import IkeaDatabase
import global_common_params
from requestprocesor import request_params
class UserBuyProcessor(object):
    def __init__(self):
        self.html_builder=HtmlBuilder()
        self.database=IkeaDatabase()

    def build_webpage_get_url(self, html_file_name):
        rst=''
        rst+=global_common_params.web_server_url
        rst+='?' + request_params.key_req_get_type + '='+request_params.val_req_get_type_webpage
        rst+='&'+request_params.key_req_get_html_file_name+'='+html_file_name

        return rst

    def process(self, intent):
        rsp_dict={}
        rsp_dict[wechat_msg_params.key_message_type] = wechat_msg_params.val_msg_type_news

        goods_name=intent.get_slot_goods_name()
        goods_filter=intent.get_slot_goods_filter()

        find_rst=self.database.find_goods(goods_name, goods_filter)

        html_file_name=self.html_builder.goods_detial_build(find_rst)

        # TODO: title, description, pic_url后期需要更新
        rsp_dict[wechat_msg_params.key_msg_content_title]='title'
        rsp_dict[wechat_msg_params.key_msg_content_description]='description'
        rsp_dict[wechat_msg_params.key_msg_content_pciurl]='https://gss0.baidu.com/7LsWdDW5_xN3otqbppnN2DJv/space/pic/item/1c950a7b02087bf429399430f8d3572c10dfcf16.jpg'
        rsp_dict[wechat_msg_params.key_msg_content_url]=self.build_webpage_get_url(html_file_name)

        return rsp_dict