#from google.appengine.ext
import webapp2
#from google.appengine.ext.webapp2.util import run_wsgi_app

i = 0

class Hello1Min(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello\n')

class Hello(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello, World!')


class Goodbye2Min(webapp2.RequestHandler):
    def get(self):
        global i
        self.response.write(i)
        i = i + 1




app = webapp2.WSGIApplication([('/', Hello), ('/hello', Hello1Min), ('/goodbye', Goodbye2Min)], debug=True)



def main():
    run_wsgi_app(application)

if __name__ == '__main__':
    run_wsgi_app(application)


