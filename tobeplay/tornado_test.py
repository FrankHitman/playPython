import tornado.web, tornado.httpclient

class MainHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def get(self, *args, **kwargs):
        http = tornado.httpclient.AsyncHTTPClient()
        http.fetch('http://www.baidu.com',
                   callback= self.on_response)

    def on_response(self, response):
        if response.error: raise tornado.web.HTTPError(500)
        self.write(response.body)
        self.finish()

c=MainHandler()
c.get()