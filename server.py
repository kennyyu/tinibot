import os
import tornado.ioloop
import tornado.web
import tornado.httpserver
import subprocess
import urllib2
import json

# local imports
import drinks
import arduino

PORT = 8880

class MainHandler(tornado.web.RequestHandler):

    def get(self):
        self.render("static/index.html")

class SpeechHandler(tornado.web.RequestHandler):

    def set_default_headers(self):
        # TODO change this to your own domain
        self.set_header("Access-Control-Allow-Origin", "https://localhost:%d" % PORT)

    def post(self):
        data = urllib2.unquote(self.request.body)
        values = json.loads(data)["values"]
        values = sorted(values, key=lambda v: v["confidence"], reverse=True)
        print values
        text = values[0]["text"].lower()
        confidence = values[0]["confidence"]
        print "GOT: %s, %f" % (text, confidence)
        drink = drinks.find_drink(text)
        if drink != "":
            subprocess.call(("say 'you said %s. I will make the drink now.'" % text).split())
            times = drinks.get_times(drink)
            arduino.send_times(times)
            subprocess.call(("say enjoy your drink!").split())
        else:
            subprocess.call(("say I don't recognize this drink: %s" % text).split())
        self.write("OK")

class DrinksHandler(tornado.web.RequestHandler):

    def get(self):
        self.write(json.dumps(drinks.DRINKS))

class StartHandler(tornado.web.RequestHandler):

    def get(self):
        subprocess.call(("say what drink would you like?").split())
        self.write("OK")

class UnknownHandler(tornado.web.RequestHandler):

    def get(self):
        subprocess.call(("say I don't know what you said, please try again.").split())
        self.write("OK")

settings = {
    "static_path": os.path.join(os.path.dirname(__file__), "static"),
}

application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/start", StartHandler),
    (r"/unknown", UnknownHandler),
    (r"/drinks", DrinksHandler),
    (r"/speech", SpeechHandler),
    (r"/static", tornado.web.StaticFileHandler, dict(path=settings['static_path'])),
], **settings)

if __name__ == "__main__":
    print "[INFO] starting server on port %d" % PORT
    print "[INFO] arduino connected on device: %s" % arduino.DEVICE
    print "[INFO] visit https://localhost:%d in chrome..." % PORT
    http_server = tornado.httpserver.HTTPServer(application, ssl_options = {
            "certfile": os.path.join("certs/server.crt"),
            "keyfile": os.path.join("certs/server_nopw.key"),
    })
    #application.listen(PORT)
    http_server.listen(8880)
    tornado.ioloop.IOLoop.instance().start()
