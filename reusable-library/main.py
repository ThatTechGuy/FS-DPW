'''
Name: Rick Martin
Class: DPW1507
Assignment: Reusable Library
'''

import webapp2
#Import all classes from both view and models
from pages import *
from library import *

class MainHandler(webapp2.RequestHandler):
    def get(self):
        #With GET variables we'll instantiate the record page and pass GET to the SETTER While also calling load from inheritence
        if self.request.GET:
            this = Record()
            this.record = self.request.GET
            display = RecordPage(this.record)
        #Without GET we simply run basic load on Default page
        else:
            display = DefaultPage()
        self.response.write(display.load())

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
