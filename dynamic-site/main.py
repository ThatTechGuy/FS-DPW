'''
Name: Rick Martin
Class: DPW1507
Assignment: Dynamic Site
'''

import webapp2
from data import *
from page import *
from lib import *

class MainHandler(webapp2.RequestHandler):
    def get(self):
        compiler = DataCompiler()
        #If we have var, instantiate compiler and pass to DataTrojan GETTER
        if self.request.GET['op']:
            compiler.push = DataTrojan(self.request.GET['op'])
            #After compiling send to OP page with full dictionary for formatting
            display = OperationPage(compiler.pull)
        else:
            #Without GET var load LandingPage with compiler GETTER for pages
            display = LandingPage(compiler.config)
        #Load Page by calling base load inherited from Default incorporating hook
        self.response.write(display.load())

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
