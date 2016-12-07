#from google.appengine.ext
import webapp2
#from google.appengine.ext.webapp2.util import run_wsgi_app


class Hello1Min(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello\n')

class Hello(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello, World!')

class Goodbye2Min(webapp2.RequestHandler):
    def get(self):
        self.response.write('Goodbye\n')



app = webapp2.WSGIApplication([('/', Hello), ('/hello', Hello1Min), ('/goodbye', Goodbye2Min)], debug=True)

#if __name__ == '__main__':
#    run_wsgi_app(application)
#
#def main():
#    run_wsgi_app(application)
