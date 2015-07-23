'''
Name: Rick Martin
Class: DPW1507
Assignment: Reusable Library
'''

import webapp2
from pages import *
from library import *

class MainHandler(webapp2.RequestHandler):
    def get(self):
        if self.request.GET:
            display = RecordPage(self.request.GET)
        else:
            display = DefaultPage()
        self.response.write(display.load())

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)