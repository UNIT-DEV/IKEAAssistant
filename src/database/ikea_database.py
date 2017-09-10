# coding:utf-8
'''
Created on 2017/9/3 下午11:08

@author: liucaiquan
'''
import pandas as pd
import global_common_params
import database_params


class IkeaDatabase(object):
    def __init__(self):
        # 最大的item书面
        self.max_item=10;
        self.goods_database_path = global_common_params.project_root_path + '/static/data.csv'
        self.goods_data = pd.read_csv(self.goods_database_path)

        self.location_database_path = global_common_params.project_root_path + '/static/locations.csv'
        self.location_data = pd.read_csv(self.location_database_path)

        self.departments_database_path=global_common_params.project_root_path+'/static/departments.csv'
        self.departments_data=pd.read_csv(self.departments_database_path)

    # 地点查询
    def find_location(self, intent_name):
        # 返回所有返回值的第一个
        # return self.location_data[self.location_data.location == intent_name][database_params.index].values[0]
        for index in self.departments_data.index:
            departments= self.departments_data.loc[index][database_params.department]
            if(departments.find(intent_name)!=-1):
                return self.departments_data.loc[index][database_params.index]

        # 没有位置正确的位置信息
        return -1

    # 商品名查询
    def find_goods(self, goods_name, filter):
        # return self.goods_data[self.goods_data.category == goods_name]
        # TODO: 后续需要添加filter过滤处理
        rst=[]
        cnt=0
        for index in self.goods_data.index:
            row=self.goods_data.loc[index]
            if(row[database_params.goods_name].find(goods_name)!=-1):
                item={}
                item[database_params.goods_name]=row[database_params.goods_name]
                item[database_params.goods_link]=row[database_params.goods_link]
                item[database_params.goods_broad]=row[database_params.goods_broad]
                item[database_params.goods_price]=row[database_params.goods_price]
                rst.append(item)
                cnt+=1
                if(cnt==self.max_item):
                    break
        return rst


    def test(self):
        print type(self.goods_data.category)
