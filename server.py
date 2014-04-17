import os
import tornado.ioloop
import tornado.web
import subprocess
import urllib2
import json

PORT = 8880

class MainHandler(tornado.web.RequestHandler):

    def get(self):
        self.render("static/index.html")

class SpeechHandler(tornado.web.RequestHandler):

    def set_default_headers(self):
        # TODO change this to your own domain
        self.set_header("Access-Control-Allow-Origin", "http://localhost:%d" % PORT)

    def post(self):
        data = urllib2.unquote(self.request.body)
        values = json.loads(data)["values"]
        values = sorted(values, key=lambda v: v["confidence"], reverse=True)
        print values
        text = values[0]["text"]
        confidence = values[0]["confidence"]
        print "GOT: %s, %f" % (text, confidence)
        subprocess.call(("say 'you said %s'" % text).split())
        self.write("OK")

settings = {
    "static_path": os.path.join(os.path.dirname(__file__), "static"),
}

application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/speech", SpeechHandler),
    (r"/static", tornado.web.StaticFileHandler, dict(path=settings['static_path'])),
], **settings)

if __name__ == "__main__":
    print "starting server on port %d, visit http://localhost:%d in chrome..." % (PORT, PORT)
    application.listen(PORT)
    tornado.ioloop.IOLoop.instance().start()
