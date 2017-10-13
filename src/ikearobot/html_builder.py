# coding:utf-8
'''
Created on 2017/9/9 下午5:24

@author: liucaiquan
'''

from database import database_params
import global_common_params
import uuid


class HtmlBuilder(object):
    '''
        HTML页面生成器
    '''

    def __init__(self):
        pass

    def __item_build(self, name, link, broad, price):
        '''
            商品条目生成
        '''
        str_price = str(price)
        return '<li class="product-item">' + '<a href=' + link + '>' + name + '\t' + broad + '\t￥' + str_price + '</a >' + '</li>'

    def goods_detial_build(self, goods_details):
        '''
            商品详情页面生成
                goods_details:商品详情信息
                返回值：生成的html页面文件名
        '''
        prefix = '''
                    <!DOCTYPE html>
                        <html>
                            <head>
                                <meta charset="UTF-8">
                                    <title></title>
                            </head>
                            <body>
                                <ul class="product-list">
                '''

        suffix = '''
                                </ul>
                            </body>
                        </html>
               '''

        goods_items = ''
        for item in goods_details:
            goods_items += self.__item_build(item[database_params.goods_name], item[database_params.goods_link],
                                             item[database_params.goods_broad], item[database_params.goods_price])

        html_content = prefix + goods_items + suffix

        html_file_name = str(uuid.uuid1()) + '.html'
        f_path = global_common_params.project_root_path + '/htmls/' + html_file_name
        f = open(f_path, 'w')
        f.write(html_content)
        f.close()

        return html_file_name

    def location_build(self, pic_url, description):
        '''
            商品详情页面生成
                pic_url:位置图片url
                返回值：生成的html页面文件名
        '''
        prefix = '''
                            <!DOCTYPE html>
                                <html>
                                    <head>
                                        <meta charset="UTF-8">
                                            <title></title>
                                    </head>
                                    <body>
                                        <div align=center>
                        '''

        suffix = '''
                                        </div>                    
                                    </body>
                                </html>
                       '''
        img = '<img width="100%" src=' + pic_url + '/>'

        description = '<p style="font-size:32px">' + description + '</p>'

        html_content = prefix + img + description + suffix

        html_file_name = str(uuid.uuid1()) + '.html'
        f_path = global_common_params.project_root_path + '/htmls/' + html_file_name
        f = open(f_path, 'w')
        f.write(html_content)
        f.close()

        return html_file_name
