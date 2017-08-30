# coding:utf-8

# from nlu.nlu_processor import NluProcessor
#
# nlu_processor=NluProcessor()
#
# rst=nlu_processor.process('今天深圳天气怎么样')
#
# print  rst

#######################
from baiduunit.unit import BaiduUnit
import json
unit=BaiduUnit()

# print unit.get_token()

query="卫生间怎么去"
rst= unit.query_request(9633, query, "").text

json_object=json.loads(rst)
print json_object
result=json_object['result']
schema= result['schema']
print schema['intent_confidence']