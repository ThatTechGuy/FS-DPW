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
        if self.request.GET['op']:
            compiler = DataCompiler()
            compiler.push = DataTrojan(self.request.GET['op'])
            display = OperationPage(compiler.pull)
        else:
            display = LandingPage()
        self.response.write(display.load())

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
