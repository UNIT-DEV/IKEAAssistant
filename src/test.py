# coding:utf-8
# #核心模块NluProcessor测试
# from nlu.nlu_processor import NluProcessor
#
# nlu_processor=NluProcessor()
# query='洗手间怎么去'
# rst=nlu_processor.process(query)
#
# print rst

#######################
# 百度UNIT接口测试
from baiduunit.baidu_unit import BaiduUnit
import json

unit = BaiduUnit()
#
print 'unit token= ', unit.get_token()
# #
# query="洗手间在那儿"
# rst= unit.query_request(9633, query, "").text
# print rst
#
# json_object=json.loads(rst)
# # print json_object
# result=json_object['result']
# schema= result['schema']

# print schema['intent_confidence']

########################
## csv文件读取和检索测试
# from database.ikea_database import IkeaDatabase
#
# database = IkeaDatabase()
# # print database.find_goods('床罩')
#
# tmp= database.find_location('内配件')
# print type(tmp)
# print tmp

#############3
# from ikearobot.html_builder import HtmlBuilder
# builder=HtmlBuilder()
#
# goods_details={}
# goods_details['name']='name'
# goods_details['link']='http://www.baidu.com'
# goods_details['broad']='broad'
# goods_details['price']='price'
#
# list=[]
# list.append(goods_details)
# list.append(goods_details)
# list.append(goods_details)
# list.append(goods_details)
# list.append(goods_details)
# html_filename=builder.build(list)
# print html_filename

##################
# a='1|2|3|4'
#
# b=a.split('|')
#
# print type(b)
# print b
