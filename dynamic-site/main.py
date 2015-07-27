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
        this = DataTrojan()
        compiler = DataCompiler
        compiler.push = this.data
        display = HomePage(compiler.pull)
        self.response.write(display.load())

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
