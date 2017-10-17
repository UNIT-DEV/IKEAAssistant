# coding:utf-8
'''
Created on 2017/9/3 下午11:08

@author: liucaiquan
'''
import pandas as pd
import global_common_params
import database_params
import re


class IkeaDatabase(object):
    '''
        IKEA数据库管理
    '''

    def __init__(self):
        # 最大的item书面
        self.goods_database_path = global_common_params.project_root_path + '/static/data.csv'
        self.goods_data = pd.read_csv(self.goods_database_path)

        self.location_database_path = global_common_params.project_root_path + '/static/locations.csv'
        self.location_data = pd.read_csv(self.location_database_path)

        self.departments_database_path = global_common_params.project_root_path + '/static/departments.csv'
        self.departments_data = pd.read_csv(self.departments_database_path)

    def find_location(self, intent_name):
        '''
            位置查询
                intent_name:位置/意图名字
                返回值：位置索引值（整型）和位置的描述信息
        '''
        print 'intent_name=', intent_name
        # 返回所有返回值的第一个

        # 在data.csv中搜索商品名，然后再在location.csv中搜索位置区域信息,最后在department中找到位置描述信息
        category = ''
        for index in self.goods_data.index:
            # print 'goods_data.index=', index
            name = self.goods_data.loc[index][database_params.goods_name]
            if name.find(intent_name) != -1:
                category = self.goods_data.loc[index][database_params.category]
                break
        print 'category=', category

        if category:
            for index in self.location_data.index:
                location_category = self.location_data.loc[index][database_params.category]
                # print 'category=', category, 'location_category=', location_category
                if category == location_category:
                    rst_index = self.location_data.loc[index][database_params.index]
                    rst_description = self.departments_data.loc[rst_index - 1][database_params.description]
                    print 'category_index=', rst_index, 'description=', rst_description
                    return rst_index, rst_description

        # 直接在department.csv中搜索区域和intent
        for index in self.departments_data.index:
            # 使用department关键字进行搜索
            departments = self.departments_data.loc[index][database_params.department]
            if departments.find(intent_name) != -1:
                return self.departments_data.loc[index][database_params.index], self.departments_data.loc[index][
                    database_params.description]

            # 使用intent关键字进行匹配
            intent = str(self.departments_data.loc[index][database_params.intent])
            if not intent:
                continue

            print 'intent= ', intent

            intent = intent.split('|')
            for keyword in intent:
                if intent_name.find(keyword) != -1:
                    return self.departments_data.loc[index][database_params.index], self.departments_data.loc[index][
                        database_params.description]

        # 没有位置正确的位置信息
        return -1, ''

    def __find_goods_new_discount(self, goods_name, goods_filter):
        '''
            以商品是否为最新，是否打折为过滤条件进行商品查找
                goods_name:需要查询的商品名
                filter：商品过滤条件
                返回值：符合条件的商品信息（list）
        '''
        rst = []
        for index in self.goods_data.index:
            row = self.goods_data.loc[index]
            if (row[database_params.goods_name].find(goods_name) != -1):
                # 商品是否为最新的
                if goods_filter == database_params.goods_newest:
                    if str(row[database_params.goods_newest]).strip() == 'False':
                        continue

                # 商品是否为打折的
                if goods_filter == database_params.goods_discount:
                    if str(row[database_params.goods_discount]).strip() == 'False':
                        continue

                item = {}
                item[database_params.goods_name] = row[database_params.goods_name]
                item[database_params.goods_img] = row[database_params.goods_img]
                item[database_params.goods_link] = row[database_params.goods_link]
                item[database_params.goods_broad] = row[database_params.goods_broad]
                item[database_params.goods_price] = row[database_params.goods_price]
                if item not in rst:
                    rst.append(item)
        return rst

    def __find_goods_price(self, goods_name, goods_filter):
        '''
            以价格高低进行排序，并进行商品查找
                goods_name:需要查询的商品名
                filter：商品过滤条件
                返回值：符合条件的商品信息（list）
        '''
        rst = []
        for index in self.goods_data.index:
            row = self.goods_data.loc[index]
            if (row[database_params.goods_name].find(goods_name) != -1):
                item = {}
                item[database_params.goods_name] = row[database_params.goods_name]
                item[database_params.goods_img] = row[database_params.goods_img]
                item[database_params.goods_link] = row[database_params.goods_link]
                item[database_params.goods_broad] = row[database_params.goods_broad]

                price = row[database_params.goods_price]

                # print 'type(price):', type(price)
                # print 'raw price= ', price
                price = re.sub('[^0-9.,]', '', price)
                price = price.replace(',', '')

                # print 'price=', price
                # print 'len(price)=', len(price)
                # for i in range(len(price)):
                #     print'char= ', price[i]

                price_float = float(price)
                item[database_params.goods_price] = price_float
                if item not in rst:
                    rst.append(item)

        rst.sort(key=lambda obj: obj.get(database_params.goods_cheap), reverse=False)

        return rst

    def find_goods(self, goods_name, goods_filter):
        '''
            商品信息查询
                goods_name:需要查询的商品名
                filter：商品过滤条件
                返回值：符合条件的商品信息（list）
        '''
        print 'filter= ', goods_filter

        if goods_filter == database_params.goods_cheap:
            return self.__find_goods_price(goods_name, goods_filter)
        else:
            return self.__find_goods_new_discount(goods_name, goods_filter)

    def test(self):
        print type(self.goods_data.category)
