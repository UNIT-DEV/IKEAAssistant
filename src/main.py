import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        echo_str = self.get_argument('echostr', default='_ARG_DEFAULT')
        if echo_str.strip()=='_ARG_DEFAULT':
            self.write("this is MyWeChatService!")
        else:
            self.write(echo_str)

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(801)
    tornado.ioloop.IOLoop.current().start()