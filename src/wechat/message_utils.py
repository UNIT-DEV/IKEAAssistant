# coding:utf-8
'''
Created on 2017年8月20日

@author: liucaiquan
'''
from lxml import etree

from wechat import common_params


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
            if element.tag == common_params.key_to_user_name:
                dict[common_params.key_to_user_name] = element.text
            elif element.tag == common_params.key_from_user_name:
                dict[common_params.key_from_user_name] = element.text
            elif element.tag == common_params.key_create_time:
                dict[common_params.key_create_time] = element.text
            elif element.tag == common_params.key_message_type:
                dict[common_params.key_message_type] = element.text
            elif element.tag == common_params.key_content:
                dict[common_params.key_content] = element.text
            elif element.tag == common_params.key_message_id:
                dict[common_params.key_message_id] = element.text
            elif element.tag == common_params.key_recognition:
                dict[common_params.key_recognition] = element.text

        return dict

    def gen_xml(self, dict):
        root = etree.Element('xml')

        to_user_name = etree.SubElement(root, common_params.key_to_user_name)
        to_user_name.text = '<![CDATA[' + dict[common_params.key_to_user_name] + ']]>'

        from_user_name = etree.SubElement(root, common_params.key_from_user_name)
        from_user_name.text = '<![CDATA[' + dict[common_params.key_from_user_name] + ']]>'

        create_time = etree.SubElement(root, common_params.key_create_time)
        create_time.text = dict[common_params.key_create_time]

        message_type = etree.SubElement(root, common_params.key_message_type)
        message_type.text = '<![CDATA[' + dict[common_params.key_message_type] + ']]>'

        # 回复内容为文本
        print 'dict[common_params.key_rsp_msg_type]'
        print dict[common_params.key_message_type]
        if (dict[common_params.key_message_type] == common_params.val_msg_type_text):
            print '回复内容为文本'
            content = etree.SubElement(root, common_params.key_content)
            content.text = '<![CDATA[' + dict[common_params.key_content] + ']]>'
        else:
            # 回复内容为news
            print '回复内容为news'
            article_count = etree.SubElement(root, common_params.key_msg_article_count)
            article_count.text = '1'

            articles = etree.SubElement(root, common_params.key_msg_articles)

            item = etree.SubElement(articles, common_params.key_msg_item)

            title = etree.SubElement(item, common_params.key_msg_content_title)
            title.text = '<![CDATA[' + dict[common_params.key_msg_content_title] + ']]>'

            description = etree.SubElement(item, common_params.key_msg_content_description)
            description.text = '<![CDATA[' + dict[common_params.key_msg_content_description] + ']]>'

            pic_url = etree.SubElement(item, common_params.key_msg_content_pciurl)
            pic_url.text = '<![CDATA[' + dict[common_params.key_msg_content_pciurl] + ']]>'

            url = etree.SubElement(item, common_params.key_msg_content_url)
            url.text = '<![CDATA[' + dict[common_params.key_msg_content_url] + ']]>'

        return etree.tostring(root, pretty_print=True)
