# coding:utf-8
'''
Created on 2017年8月19日

@author: liucaiquan
'''
# 基本消息信息
KEY_TO_USER_NAME = 'ToUserName'
KEY_FROM_USER_NAME = 'FromUserName'
KEY_CREATE_TIME = 'CreateTime'
KEY_MESSAGE_TYPE = 'MsgType'
KEY_CONTENT = 'Content'
KEY_MESSAGE_ID = 'MsgId'
KEY_RECOGNITION = 'Recognition'

# 消息类型
VAL_MSG_TYPE_INVALID = 'invalid'
VAL_MSG_TYPE_TEXT = 'text'
VAL_MSG_TYPE_VOICE = 'voice'
VAL_MSG_TYPE_NEWS = 'news'

##################图文回复消息相关############################
# 图文消息个数
KEY_MSG_ARTICLE_COUNT = 'ArticleCount'

# 多条图文消息信息
KEY_MSG_ARTICLES = 'Articles'

# 图文消息标题
KEY_MSG_CONTENT_TITLE = 'Title'

# 图文消息描述
KEY_MSG_CONTENT_DESCRIPTION = 'Description'

# 图片链接
KEY_MSG_CONTENT_PIC_URL = 'PicUrl'

# 点击图文消息跳转链接
KEY_MSG_CONTENT_URL = 'Url'

# 用于分割的item
KEY_MSG_ITEM = 'item'
