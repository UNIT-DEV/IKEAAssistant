# coding:utf-8
'''
Created on 2017/9/5 上午11:06

@author: liucaiquan
'''
import threading
import logging

# logger打印等级
# LOGGER_LEVEL = logging.INFO
LOGGER_LEVEL=logging.ERROR

# 工程根目录位置
project_root_path = '/opt/IKEAAssistant'
# project_root_path = '..'

# webserver端口
server_port = 80

# webserver地址
# web_server_url='http://120.25.220.14'
web_server_url = 'http://www.eddy2017.com'

# 最大并发线程数目(超过最大并发数，请求丢弃)
max_concurrent_thread_num = 10
# 当前线程池中线程数目
current_thread_num = 0
# http请求锁
request_lock = threading.Lock()
# 线程计数器锁
thread_cnt_lock = threading.Lock()
