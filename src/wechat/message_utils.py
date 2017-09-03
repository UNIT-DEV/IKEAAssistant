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
            if element.tag == common_params.to_user_name:
                dict[common_params.to_user_name] = element.text
            elif element.tag == common_params.from_user_name:
                dict[common_params.from_user_name] = element.text
            elif element.tag == common_params.create_time:
                dict[common_params.create_time] = element.text
            elif element.tag == common_params.message_type:
                dict[common_params.message_type] = element.text
            elif element.tag == common_params.content:
                dict[common_params.content] = element.text
            elif element.tag == common_params.message_id:
                dict[common_params.message_id] = element.text
            elif element.tag==common_params.recognition:
                dict[common_params.recognition]=element.text

        return dict

    def gen_xml(self, dict):
        root = etree.Element('xml')

        to_user_name = etree.SubElement(root, common_params.to_user_name)
        to_user_name.text = '<![CDATA[' + dict[common_params.to_user_name] + ']]>'

        to_user_name = etree.SubElement(root, common_params.from_user_name)
        to_user_name.text = '<![CDATA[' + dict[common_params.from_user_name] + ']]>'

        to_user_name = etree.SubElement(root, common_params.create_time)
        to_user_name.text = dict[common_params.create_time]

        to_user_name = etree.SubElement(root, common_params.message_type)
        to_user_name.text = '<![CDATA[' + dict[common_params.message_type] + ']]>'

        to_user_name = etree.SubElement(root, common_params.content)
        to_user_name.text = '<![CDATA[' + dict[common_params.content] + ']]>'

        #         to_user_name = etree.SubElement(root, common_params.message_id)
        #         to_user_name.text=dict[common_params.message_id]

        return etree.tostring(root, pretty_print=True)
