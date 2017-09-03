# coding:utf-8
'''
Created on 2017/9/3 下午11:08

@author: liucaiquan
'''
import pandas as pd


class IkeaDatabase(object):
    # 商品名查询
    def find_goods(self, goods):
        return self.data[self.data.category == goods]

    def __init__(self):
        self.database_path = '../static/data.csv'
        self.data = pd.read_csv(self.database_path)
