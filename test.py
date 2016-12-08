import json
import time
import webapp2
from firebase import firebase, jsonutil


class DailyMaintanence(webapp2.RequestHandler):
    def get(self):
        fb = firebase.FirebaseApplication('https://skwad-729af.firebaseio.com', None)
            packs = fb.get('/packs', None)
            
            if packs is not None:
                for location in packs:
                    for pack_id in packs[location]:
                        pack = packs[location][pack_id]
                        
                        print "Pack Name:", pack['name']
                        print "Description:", pack['desc']
                        print "Lat:", pack['lat']
                        print "Lon:", pack['lon']
                        print "Time:", pack['time']
                        
                        t_delta = time.time()-float(pack['time'])
                        t_remain = 86400-t_delta
                        
                        if t_remain <= 0:
                            fb.delete("/".join(["packs", location]), pack_id)
                            print "Pack deleted."
                        else:
                            print "Pack has %i seconds remaining." % t_remain

                    print "------------------------------------------"


class Main(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello')


app = webapp2.WSGIApplication([('/', Main), ('/dailyData', DailyMaintanence)], debug=True)


def main():
    run_wsgi_app(app)


if __name__ == "__main__":
    run_wsgi_app(app)
