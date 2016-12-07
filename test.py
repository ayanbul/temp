from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

class ParseXMLHandler(webapp.RequestHandler):
    def get(self):
        print "Hello\n"

application = webapp.WSGIApplication([('/tasks/data', ParseXMLHandler)], debug=True)

if __name__ == '__main__':
    print "Hello World"
    run_wsgi_app(application)

def main():
    run_wsgi_app(application)
