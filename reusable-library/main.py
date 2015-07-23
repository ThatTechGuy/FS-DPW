'''
Name: Rick Martin
Class: DPW1507
Assignment: Reusable Library
'''

import webapp2
from pages import *

class MainHandler(webapp2.RequestHandler):
    def get(self):
        home_page = DefaultPage()
        self.response.write(home_page.load())

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
