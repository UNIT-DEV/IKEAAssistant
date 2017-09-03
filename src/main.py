# coding:utf-8
'''
Created on 2017年8月19日

@author: liucaiquan

基于Tornado的Web Server启动入口
'''
import tornado.ioloop
import tornado.web
from requestprocesor.request_processor import RequestProcessor


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        # 'echostr'字段用于微信后台服务的配置绑定
        echo_str = self.get_argument('echostr', default='_ARG_DEFAULT')
        if echo_str.strip() == '_ARG_DEFAULT':
            request_processor.get(self)
        else:
            self.write(echo_str)

    def post(self):
        request_processor.post(self)


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])


def init():
    global request_processor
    request_processor = RequestProcessor()


if __name__ == "__main__":
    init()

    app = make_app()
    app.listen(80)
    tornado.ioloop.IOLoop.current().start()
