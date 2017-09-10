# coding:utf-8
'''
Created on 2017年8月19日

@author: liucaiquan

基于Tornado的Web Server启动入口
'''
import tornado.ioloop
import tornado.web
from requestprocesor.request_processor import RequestProcessor
import global_common_params
import threading
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


class MainHandler(tornado.web.RequestHandler):
    def __add_to_tread_pool(self, req, request_type):
        # global_common_params.thread_cnt_lock.acquire()
        # if (global_common_params.current_thread_num >= global_common_params.max_concurrent_thread_num):
        #     global_common_params.thread_cnt_lock.release()
        #     print 'warning: 已超过最大并发线程数目'
        #     return
        #
        # global_common_params.current_thread_num += 1
        # global_common_params.thread_cnt_lock.release()

        # request_processor = RequestProcessor()
        if (request_type == 'get'):
            # t = threading.Thread(target=request_processor.get_processor, args=(req,))
            request_processor.get_processor(req)
        else:
            # t = threading.Thread(target=request_processor.post_processor, args=(req,))
            request_processor.post_processor(req)

            # t.setDaemon(True)
            # t.start()

    def get(self):
        # global_common_params.request_lock.acquire()
        self.__add_to_tread_pool(self, 'get')
        # global_common_params.request_lock.release()

    def post(self):
        # global_common_params.request_lock.acquire()
        self.__add_to_tread_pool(self, 'post')
        # global_common_params.request_lock.release()


def __make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])


def __init():
    global request_processor
    request_processor = RequestProcessor()

    # global request_lock
    # request_lock = threading.Lock()


if __name__ == "__main__":
    __init()

    app = __make_app()
    app.listen(global_common_params.server_port)
    tornado.ioloop.IOLoop.current().start()
