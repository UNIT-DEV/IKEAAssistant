# coding:utf-8
'''
Created on 2017/9/5 上午11:06

@author: liucaiquan
'''
import threading
import logging

# logger打印等级
# LOGGER_LEVEL = logging.INFO
LOGGER_LEVEL = logging.ERROR

# 工程根目录位置
PROJECT_ROOT_PATH = '/opt/IKEAAssistant'
# project_root_path = '..'

# webserver端口
SERVER_PORT = 80

# webserver地址
# web_server_url='http://120.25.220.14'
WEB_SERVER_URL = 'http://www.eddy2017.com'

# 最大并发线程数目(超过最大并发数，请求丢弃)
MAX_CONCURRENT_THREAD_NUM = 10
# 当前线程池中线程数目
CURRENT_THREAD_NUM = 0
# http请求锁
REQUEST_LOCK = threading.Lock()
# 线程计数器锁
THREAD_CNT_LOCK = threading.Lock()

# IKEAAssistant功能开关
IKEA_ASSISTANT_SWITCH = False
