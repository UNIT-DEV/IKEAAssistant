# coding:utf-8
'''
Created on 2017/9/9 下午3:18

@author: liucaiquan
'''
import wechat.wechat_msg_params as wechat_msg_params
import ikearobot.ikearobot_params as ikearobot_params
import requestprocesor.request_params as request_params
import global_common_params

from database.ikea_database import IkeaDatabase
from ikearobot.html_builder import HtmlBuilder


class UserLocationProcessor(object):
    '''
        位置意图查询
    '''
    database = IkeaDatabase()

    def __init__(self):
        # self.database = IkeaDatabase()
        self.html_builder = HtmlBuilder()

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
            位置意图处理
                intent：百度UNIT返回结果封装
                返回值：结果字典
        '''
        rsp_dict = {}
        rsp_dict[wechat_msg_params.KEY_MESSAGE_TYPE] = wechat_msg_params.VAL_MSG_TYPE_INVALID

        location = intent.get_slot_location()

        # slot中没有位置信息
        if location is None:
            rsp_dict[wechat_msg_params.KEY_MESSAGE_TYPE] = wechat_msg_params.VAL_MSG_TYPE_TEXT
            rsp_dict[wechat_msg_params.KEY_CONTENT] = u'抱歉，没有找到您需要查找的位置~'
            return rsp_dict

        index, description = self.database.find_location(location)

        # 位置信息无效
        if (index <= 0):
            rsp_dict[wechat_msg_params.KEY_MESSAGE_TYPE] = wechat_msg_params.VAL_MSG_TYPE_TEXT
            rsp_dict[wechat_msg_params.KEY_CONTENT] = u'抱歉，没有找到您需要查找的位置~'
            return rsp_dict

        html_file_name = self.html_builder.location_build(ikearobot_params.PIC_RESOURCE_DICT[index], description)

        rsp_dict[wechat_msg_params.KEY_MESSAGE_TYPE] = wechat_msg_params.VAL_MSG_TYPE_NEWS
        rsp_dict[wechat_msg_params.KEY_MSG_CONTENT_TITLE] = location + u'位置信息'
        rsp_dict[wechat_msg_params.KEY_MSG_CONTENT_DESCRIPTION] = u'点击查看详细的位置信息'
        rsp_dict[wechat_msg_params.KEY_MSG_CONTENT_PIC_URL] = ikearobot_params.PIC_RESOURCE_DICT[index]
        rsp_dict[wechat_msg_params.KEY_MSG_CONTENT_URL] = self.__build_webpage_get_url(html_file_name)
        return rsp_dict
