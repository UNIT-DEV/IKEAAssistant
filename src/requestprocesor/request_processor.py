#coding:utf-8
'''
Created on 2017年8月19日

@author: liucaiquan
'''

class RequestProcessor(object):
    '''
    classdocs
    '''
    def get(self, requst):
        requst.write("this is MyWeChatService!")
        

    def post(self, request):
        pass
    
    def __init__(self):
        '''
        Constructor
        '''
        