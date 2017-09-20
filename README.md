# IKEA Assistant
宜家购物小助手是一个微信公众号，借助百度UNIT自然语言处理平台，通过文本和语音输入的形式，帮助购物用户快速寻找位置和查询商品，提高用户购物体验。当前测试数据为真实的宜家数据，通过爬虫从宜家官网获取。
## 运行环境
服务器：阿里云ECS
WebServer：Tornado
开发语言：Python
## 当前进度
* 微信公众号（个人）的后台绑定
* 微信后台请求解析与回复封装
* Turing机器人后台接口接入（兜底策略）
* 百度UNIT意图/词槽解析接入(完成IKEA相关意图和词槽的解析和封装) 
* 通过shell脚本实现系统的启动(后台运行)和退出
* 支持微信语音输入
* 支持图文类型信息回复
* 支持位置查询（如，怎么去衣柜区？卫生间在什么地方？）
* 支持商品信息查询（如，推荐几款最便宜的椅子？）
* 支持图文页面动态生成
## 启动命令
  sudo ./start_wechat_server.sh
## 退出命令
  sudo ./stop_wechat_server.sh
## 关注微信二维码进行体验(任意一个均可)

![](./static/github/Wechat_Pan.png)

![](./static/github/MyAI_Wechat_QRC.png)

## 演示视频
<http://v.youku.com/v_show/id_XMzAzNTY1NzYwNA==.html?spm=a2hzp.8244740.0.0#paction>
