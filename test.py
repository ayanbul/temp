#from google.appengine.ext
import webapp2
#from google.appengine.ext.webapp2.util import run_wsgi_app

class Cron(webapp2.RequestHandler):
    def get(self):
        print "Hello\n"

class Hello(webapp2.RequestHandler):
    def get(self):
        print "Hello, World!"

app = webapp2.WSGIApplication([('/', Hello), ('/tasks/data', Cron)], debug=True)

#if __name__ == '__main__':
#    run_wsgi_app(application)
#
#def main():
#    run_wsgi_app(application)
