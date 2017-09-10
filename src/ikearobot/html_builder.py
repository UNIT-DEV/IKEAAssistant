# coding:utf-8
'''
Created on 2017/9/9 下午5:24

@author: liucaiquan
'''

from database import database_params
import global_common_params
import uuid
class HtmlBuilder(object):
    def __init__(self):
        pass
    def item_build(self, name, link, broad, price):
        return '<li class="product-item">'+'<a href=' + link + '>' + name + '\t' + broad + '\t' + price + '</a >'+'</li>'

    # 商品详情页面生成
    def goods_detial_build(self, goods_details):
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

        goods_items=''
        for item in goods_details:
            goods_items+= self.item_build(item[database_params.goods_name], item[database_params.goods_link], item[database_params.goods_broad], item[database_params.goods_price])

        html_content=prefix+goods_items+suffix

        html_file_name=str(uuid.uuid1())+'.html'
        f_path=global_common_params.project_root_path+'/htmls/'+html_file_name
        f=open(f_path, 'w')
        f.write(html_content)
        f.close()

        return html_file_name


    # 位置页面生成
    def location_build(self, pic_url):
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
        img='<img src='+pic_url+'/>'

        html_content = prefix + img + suffix

        html_file_name = str(uuid.uuid1()) + '.html'
        f_path = global_common_params.project_root_path + '/htmls/' + html_file_name
        f = open(f_path, 'w')
        f.write(html_content)
        f.close()

        return html_file_name
