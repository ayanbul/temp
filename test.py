from google.appengine.ext import webapp2
from google.appengine.ext.webapp.util import run_wsgi_app

class TestHandler(webapp2.RequestHandler):
    def get(self):
        print "Hello\n"

application = webapp2.WSGIApplication([('/tasks/data', TestHandler)], debug=True)

if __name__ == '__main__':
    print "Hello World\n"
    run_wsgi_app(application)

def main():
    run_wsgi_app(application)
