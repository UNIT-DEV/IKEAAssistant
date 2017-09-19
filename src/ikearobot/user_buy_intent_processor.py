# coding:utf-8
'''
Created on 2017/9/9 下午3:19

@author: liucaiquan
'''
import ikearobot_params
from html_builder import HtmlBuilder
from wechat import wechat_msg_params
from database.ikea_database import IkeaDatabase
import global_common_params
from requestprocesor import request_params


class UserBuyProcessor(object):
    '''
        商品详情查询处理
    '''

    def __init__(self):
        self.html_builder = HtmlBuilder()
        self.database = IkeaDatabase()

    '''
        页面url地址生成
            html_file_name: 文件名
            返回值：完整的url地址字符串
    '''

    def __build_webpage_get_url(self, html_file_name):
        rst = ''
        rst += global_common_params.web_server_url
        rst += '?' + request_params.key_req_get_type + '=' + request_params.val_req_get_type_webpage
        rst += '&' + request_params.key_req_get_html_file_name + '=' + html_file_name

        return rst

    '''
        商品详情意图处理
            intent：百度UNIT返回结果封装
            返回值：结果字典
    '''

    def process(self, intent):
        rsp_dict = {}
        rsp_dict[wechat_msg_params.key_message_type] = wechat_msg_params.val_msg_type_invalid

        goods_name = intent.get_slot_goods_name()
        # unit中没有商品名的slog
        if goods_name is None:
            return rsp_dict
        goods_filter_type, goods_filter_content = intent.get_slot_goods_filter()

        find_rst = self.database.find_goods(goods_name, goods_filter_type)

        html_file_name = self.html_builder.goods_detial_build(find_rst)

        rsp_dict[wechat_msg_params.key_message_type] = wechat_msg_params.val_msg_type_news

        if goods_filter_content:
            rsp_dict[wechat_msg_params.key_msg_content_title] = str(goods_filter_content) + u'的' + str(
                goods_name) + u'详情'
        else:
            rsp_dict[wechat_msg_params.key_msg_content_title] = str(goods_name) + u'详情'
        rsp_dict[wechat_msg_params.key_msg_content_description] = u'点击查看商品详情'
        rsp_dict[
            wechat_msg_params.key_msg_content_pciurl] = ikearobot_params.goods_detail_title_pic_url
        rsp_dict[wechat_msg_params.key_msg_content_url] = self.__build_webpage_get_url(html_file_name)

        return rsp_dict
