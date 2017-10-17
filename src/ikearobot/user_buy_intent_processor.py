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
import database.database_params


class UserBuyProcessor(object):
    '''
        商品详情查询处理
    '''

    def __init__(self):
        self.html_builder = HtmlBuilder()
        self.database = IkeaDatabase()

    def __build_webpage_get_url(self, html_file_name):
        '''
            页面url地址生成
                html_file_name: 文件名
                返回值：完整的url地址字符串
        '''
        rst = ''
        rst += global_common_params.web_server_url
        rst += '?' + request_params.key_req_get_type + '=' + request_params.val_req_get_type_webpage
        rst += '&' + request_params.key_req_get_html_file_name + '=' + html_file_name

        return rst

    def process(self, intent):
        '''
            商品详情意图处理
                intent：百度UNIT返回结果封装
                返回值：结果字典
        '''
        rsp_dict = {}
        rsp_dict[wechat_msg_params.key_message_type] = wechat_msg_params.val_msg_type_invalid

        goods_name = intent.get_slot_goods_name()
        # unit中没有商品名的slog
        if goods_name is None:
            rsp_dict[wechat_msg_params.key_message_type] = wechat_msg_params.val_msg_type_text
            rsp_dict[wechat_msg_params.key_content] = u'抱歉，没有找到您需要查找的商品~'
            return rsp_dict
        goods_filter_type, goods_filter_content = intent.get_slot_goods_filter()

        find_rst = self.database.find_goods(goods_name, goods_filter_type)
        # 数据库中没有符合查询条件的商品
        if not find_rst:
            rsp_dict[wechat_msg_params.key_message_type] = wechat_msg_params.val_msg_type_text
            rsp_dict[wechat_msg_params.key_content] = u'抱歉，没有找到您需要查找的商品~'
            return rsp_dict

        html_file_name = self.html_builder.goods_detial_build(find_rst)

        rsp_dict[wechat_msg_params.key_message_type] = wechat_msg_params.val_msg_type_news

        if goods_filter_content:
            rsp_dict[wechat_msg_params.key_msg_content_title] = str(goods_filter_content) + u'的' + str(
                goods_name) + u'详情'
        else:
            rsp_dict[wechat_msg_params.key_msg_content_title] = str(goods_name) + u'详情'

        rsp_dict[wechat_msg_params.key_msg_content_description] = u'点击查看商品详情'
        # rsp_dict[wechat_msg_params.key_msg_content_pciurl] = ikearobot_params.goods_detail_title_pic_url

        # 挑选商品详情title图片
        for item in find_rst:
            rst_goods_name = str(item[database.database_params.goods_name])
            if rst_goods_name.endswith(goods_name):
                rsp_dict[wechat_msg_params.key_msg_content_pciurl] = item[database.database_params.goods_img]
                break
            else:
                rsp_dict[wechat_msg_params.key_msg_content_pciurl] = find_rst[0][database.database_params.goods_img]

        rsp_dict[wechat_msg_params.key_msg_content_url] = self.__build_webpage_get_url(html_file_name)

        return rsp_dict
