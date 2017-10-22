# coding:utf-8
'''
Created on 2017/9/9 下午3:19

@author: liucaiquan
'''
import global_common_params
import wechat.wechat_msg_params as wechat_msg_params
import requestprocesor.request_params as request_params
import database.database_params

from ikearobot.html_builder import HtmlBuilder
from database.ikea_database import IkeaDatabase


class UserBuyProcessor(object):
    '''
        商品详情查询处理
    '''
    database = IkeaDatabase()

    def __init__(self):
        self.html_builder = HtmlBuilder()
        # self.database = IkeaDatabase()

    def __build_webpage_get_url(self, html_file_name):
        '''
            页面url地址生成
                html_file_name: 文件名
                返回值：完整的url地址字符串
        '''
        rst = ''
        rst += global_common_params.WEB_SERVER_URL
        rst += '?' + request_params.KEY_REQ_GET_TYPE + '=' + request_params.VAL_REQ_GET_TYPE_WEBPAGE
        rst += '&' + request_params.KEY_REQ_GET_HTML_FILE_NAME + '=' + html_file_name

        return rst

    def process(self, intent):
        '''
            商品详情意图处理
                intent：百度UNIT返回结果封装
                返回值：结果字典
        '''
        rsp_dict = {}
        rsp_dict[wechat_msg_params.KEY_MESSAGE_TYPE] = wechat_msg_params.VAL_MSG_TYPE_INVALID

        goods_name = intent.get_slot_goods_name()
        # unit中没有商品名的slog
        if goods_name is None:
            rsp_dict[wechat_msg_params.KEY_MESSAGE_TYPE] = wechat_msg_params.VAL_MSG_TYPE_TEXT
            rsp_dict[wechat_msg_params.KEY_CONTENT] = u'抱歉，没有找到您需要查找的商品~'
            return rsp_dict
        goods_filter_type, goods_filter_content = intent.get_slot_goods_filter()

        find_rst = self.database.find_goods(goods_name, goods_filter_type)
        # 数据库中没有符合查询条件的商品
        if not find_rst:
            rsp_dict[wechat_msg_params.KEY_MESSAGE_TYPE] = wechat_msg_params.VAL_MSG_TYPE_TEXT
            rsp_dict[wechat_msg_params.KEY_CONTENT] = u'抱歉，没有找到您需要查找的商品~'
            return rsp_dict

        html_file_name = self.html_builder.goods_detial_build(find_rst)

        rsp_dict[wechat_msg_params.KEY_MESSAGE_TYPE] = wechat_msg_params.VAL_MSG_TYPE_NEWS

        if goods_filter_content:
            rsp_dict[wechat_msg_params.KEY_MSG_CONTENT_TITLE] = str(goods_filter_content) + u'的' + str(
                goods_name) + u'详情'
        else:
            rsp_dict[wechat_msg_params.KEY_MSG_CONTENT_TITLE] = str(goods_name) + u'详情'

        rsp_dict[wechat_msg_params.KEY_MSG_CONTENT_DESCRIPTION] = u'点击查看商品详情'
        # rsp_dict[wechat_msg_params.key_msg_content_pciurl] = ikearobot_params.goods_detail_title_pic_url

        # 挑选商品详情title图片
        for item in find_rst:
            rst_goods_name = str(item[database.database_params.GOODS_NAME])
            if rst_goods_name.endswith(goods_name):
                rsp_dict[wechat_msg_params.KEY_MSG_CONTENT_PIC_URL] = item[database.database_params.GOODS_IMG]
                break
            else:
                rsp_dict[wechat_msg_params.KEY_MSG_CONTENT_PIC_URL] = find_rst[0][database.database_params.GOODS_IMG]

        rsp_dict[wechat_msg_params.KEY_MSG_CONTENT_URL] = self.__build_webpage_get_url(html_file_name)

        return rsp_dict
