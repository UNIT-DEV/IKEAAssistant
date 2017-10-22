# coding:utf-8
'''
Created on 2017年8月20日

@author: liucaiquan
'''
import logging
import lxml.etree as etree

import wechat.wechat_msg_params as wechat_msg_params
import global_common_params

logging.basicConfig(level=global_common_params.LOGGER_LEVEL)


class MessageUtil(object):
    '''
    微信接口信息解析和封装
    '''

    def __init__(self):
        '''
        Constructor
        '''

    def parse_xml(self, request_body):
        '''
            微信请求解析
                request：微信请求句柄
                返回信息dict
        '''
        xml_content = request_body
        root = etree.fromstring(xml_content)

        dict = {}
        for element in root.iter("*"):
            if element.tag == wechat_msg_params.KEY_TO_USER_NAME:
                dict[wechat_msg_params.KEY_TO_USER_NAME] = element.text
            elif element.tag == wechat_msg_params.KEY_FROM_USER_NAME:
                dict[wechat_msg_params.KEY_FROM_USER_NAME] = element.text
            elif element.tag == wechat_msg_params.KEY_CREATE_TIME:
                dict[wechat_msg_params.KEY_CREATE_TIME] = element.text
            elif element.tag == wechat_msg_params.KEY_MESSAGE_TYPE:
                dict[wechat_msg_params.KEY_MESSAGE_TYPE] = element.text
            elif element.tag == wechat_msg_params.KEY_CONTENT:
                dict[wechat_msg_params.KEY_CONTENT] = element.text
            elif element.tag == wechat_msg_params.KEY_MESSAGE_ID:
                dict[wechat_msg_params.KEY_MESSAGE_ID] = element.text
            elif element.tag == wechat_msg_params.KEY_RECOGNITION:
                dict[wechat_msg_params.KEY_RECOGNITION] = element.text

        return dict

    def gen_xml(self, dict):
        '''
            微信返回结果生成
                dict：返回的微信信息内容
                返回值：XML格式字符串
        '''
        root = etree.Element('xml')

        to_user_name = etree.SubElement(root, wechat_msg_params.KEY_TO_USER_NAME)
        to_user_name.text = '<![CDATA[' + dict[wechat_msg_params.KEY_TO_USER_NAME] + ']]>'

        from_user_name = etree.SubElement(root, wechat_msg_params.KEY_FROM_USER_NAME)
        from_user_name.text = '<![CDATA[' + dict[wechat_msg_params.KEY_FROM_USER_NAME] + ']]>'

        create_time = etree.SubElement(root, wechat_msg_params.KEY_CREATE_TIME)
        create_time.text = dict[wechat_msg_params.KEY_CREATE_TIME]

        message_type = etree.SubElement(root, wechat_msg_params.KEY_MESSAGE_TYPE)
        message_type.text = '<![CDATA[' + dict[wechat_msg_params.KEY_MESSAGE_TYPE] + ']]>'

        # 回复内容为文本
        # print 'dict[common_params.key_rsp_msg_type]'
        # print dict[wechat_msg_params.key_message_type]
        logging.info('dict[common_params.key_rsp_msg_type]= {}'.format(dict[wechat_msg_params.KEY_MESSAGE_TYPE]))
        if (dict[wechat_msg_params.KEY_MESSAGE_TYPE] == wechat_msg_params.VAL_MSG_TYPE_TEXT):
            # print '回复内容为文本'
            logging.info('回复内容为文本')
            content = etree.SubElement(root, wechat_msg_params.KEY_CONTENT)
            content.text = '<![CDATA[' + dict[wechat_msg_params.KEY_CONTENT] + ']]>'
        else:
            # 回复内容为news
            # print '回复内容为news'
            logging.info('回复内容为news')
            article_count = etree.SubElement(root, wechat_msg_params.KEY_MSG_ARTICLE_COUNT)
            article_count.text = '1'

            articles = etree.SubElement(root, wechat_msg_params.KEY_MSG_ARTICLES)

            item = etree.SubElement(articles, wechat_msg_params.KEY_MSG_ITEM)

            title = etree.SubElement(item, wechat_msg_params.KEY_MSG_CONTENT_TITLE)
            title.text = '<![CDATA[' + dict[wechat_msg_params.KEY_MSG_CONTENT_TITLE] + ']]>'

            description = etree.SubElement(item, wechat_msg_params.KEY_MSG_CONTENT_DESCRIPTION)
            description.text = '<![CDATA[' + dict[wechat_msg_params.KEY_MSG_CONTENT_DESCRIPTION] + ']]>'

            pic_url = etree.SubElement(item, wechat_msg_params.KEY_MSG_CONTENT_PIC_URL)
            pic_url.text = '<![CDATA[' + dict[wechat_msg_params.KEY_MSG_CONTENT_PIC_URL] + ']]>'

            url = etree.SubElement(item, wechat_msg_params.KEY_MSG_CONTENT_URL)
            url.text = '<![CDATA[' + dict[wechat_msg_params.KEY_MSG_CONTENT_URL] + ']]>'

        return etree.tostring(root, pretty_print=True)
