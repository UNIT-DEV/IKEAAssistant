# coding:utf-8
'''
Created on 2017年8月19日

@author: liucaiquan

基于Tornado的Web Server启动入口
'''
import sys
import tornado.ioloop
import tornado.web
import global_common_params

from concurrent.futures import ThreadPoolExecutor
from tornado.concurrent import run_on_executor
from requestprocesor.request_processor import RequestProcessor
import requestprocesor.request_params as request_params

reload(sys)
sys.setdefaultencoding('utf-8')


class MainHandler(tornado.web.RequestHandler):
    executor = ThreadPoolExecutor(20)

    @run_on_executor
    def get_thread(self, html_file):
        request_processor = RequestProcessor()
        return request_processor.get_processor(html_file)

    @run_on_executor
    def post_thread(self, request_body):
        request_processor = RequestProcessor()
        rst = request_processor.post_processor(request_body)
        return rst

    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def get(self):
        '''
            get请求处理
        '''

        echo_str = self.get_argument('echostr', default='_ARG_DEFAULT')
        # 返回微信认证信息
        if echo_str.strip() != '_ARG_DEFAULT':
            self.write(echo_str)
        else:
            htmp_file_name = self.get_argument(request_params.KEY_REQ_GET_HTML_FILE_NAME, default='_ARG_DEFAULT')
            # 普通域名访问
            if htmp_file_name == '_ARG_DEFAULT':
                self.write('this is a tornador web server!')
            else:
                # 商品详情html文件获取
                get_process_rst = yield self.get_thread(htmp_file_name)
                self.render(get_process_rst)
                # self.finish()

    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def post(self):
        '''
            post请求处理
        '''

        request_body = self.request.body

        post_process_rst = yield self.post_thread(request_body)
        self.write(post_process_rst)


def __make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])


if __name__ == "__main__":
    app = __make_app()
    app.listen(global_common_params.SERVER_PORT)
    tornado.ioloop.IOLoop.current().start()
