# coding=utf-8
import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Booraga! Bonjour, 曾冠傑!')

app = webapp2.WSGIApplication([('/', MainPage)],
                              debug=True)
