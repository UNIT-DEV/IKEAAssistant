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
##百度UNIT接口测试
# from baiduunit.unit import BaiduUnit
# import json
# unit=BaiduUnit()
#
# # print unit.get_token()
#
# query="洗手间怎么去"
# rst= unit.query_request(9633, query, "").text
# print rst
#
# json_object=json.loads(rst)
# # print json_object
# result=json_object['result']
# schema= result['schema']
#
# # print schema['intent_confidence']

########################
## csv文件读取和检索测试
from database.ikea_database import IkeaDatabase

database = IkeaDatabase()
print database.find_goods('床罩')
