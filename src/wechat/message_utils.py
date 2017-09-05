# coding:utf-8
'''
Created on 2017年8月20日

@author: liucaiquan
'''
from lxml import etree

from wechat import wechat_msg_params


class MessageUtil(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''

    def parse_xml(self, request):
        xml_content = request.request.body
        root = etree.fromstring(xml_content)

        dict = {}
        for element in root.iter("*"):
            if element.tag == wechat_msg_params.key_to_user_name:
                dict[wechat_msg_params.key_to_user_name] = element.text
            elif element.tag == wechat_msg_params.key_from_user_name:
                dict[wechat_msg_params.key_from_user_name] = element.text
            elif element.tag == wechat_msg_params.key_create_time:
                dict[wechat_msg_params.key_create_time] = element.text
            elif element.tag == wechat_msg_params.key_message_type:
                dict[wechat_msg_params.key_message_type] = element.text
            elif element.tag == wechat_msg_params.key_content:
                dict[wechat_msg_params.key_content] = element.text
            elif element.tag == wechat_msg_params.key_message_id:
                dict[wechat_msg_params.key_message_id] = element.text
            elif element.tag == wechat_msg_params.key_recognition:
                dict[wechat_msg_params.key_recognition] = element.text

        return dict

    def gen_xml(self, dict):
        root = etree.Element('xml')

        to_user_name = etree.SubElement(root, wechat_msg_params.key_to_user_name)
        to_user_name.text = '<![CDATA[' + dict[wechat_msg_params.key_to_user_name] + ']]>'

        from_user_name = etree.SubElement(root, wechat_msg_params.key_from_user_name)
        from_user_name.text = '<![CDATA[' + dict[wechat_msg_params.key_from_user_name] + ']]>'

        create_time = etree.SubElement(root, wechat_msg_params.key_create_time)
        create_time.text = dict[wechat_msg_params.key_create_time]

        message_type = etree.SubElement(root, wechat_msg_params.key_message_type)
        message_type.text = '<![CDATA[' + dict[wechat_msg_params.key_message_type] + ']]>'

        # 回复内容为文本
        print 'dict[common_params.key_rsp_msg_type]'
        print dict[wechat_msg_params.key_message_type]
        if (dict[wechat_msg_params.key_message_type] == wechat_msg_params.val_msg_type_text):
            print '回复内容为文本'
            content = etree.SubElement(root, wechat_msg_params.key_content)
            content.text = '<![CDATA[' + dict[wechat_msg_params.key_content] + ']]>'
        else:
            # 回复内容为news
            print '回复内容为news'
            article_count = etree.SubElement(root, wechat_msg_params.key_msg_article_count)
            article_count.text = '1'

            articles = etree.SubElement(root, wechat_msg_params.key_msg_articles)

            item = etree.SubElement(articles, wechat_msg_params.key_msg_item)

            title = etree.SubElement(item, wechat_msg_params.key_msg_content_title)
            title.text = '<![CDATA[' + dict[wechat_msg_params.key_msg_content_title] + ']]>'

            description = etree.SubElement(item, wechat_msg_params.key_msg_content_description)
            description.text = '<![CDATA[' + dict[wechat_msg_params.key_msg_content_description] + ']]>'

            pic_url = etree.SubElement(item, wechat_msg_params.key_msg_content_pciurl)
            pic_url.text = '<![CDATA[' + dict[wechat_msg_params.key_msg_content_pciurl] + ']]>'

            url = etree.SubElement(item, wechat_msg_params.key_msg_content_url)
            url.text = '<![CDATA[' + dict[wechat_msg_params.key_msg_content_url] + ']]>'

        return etree.tostring(root, pretty_print=True)
