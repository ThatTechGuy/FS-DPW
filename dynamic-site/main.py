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
        #Instantiate compiler with DataCompiler from library
        compiler = DataCompiler()
        #Instantiate multiple DataTrojans from data and pass to compiler through setter
        compiler.push = DataTrojan("who")
        compiler.push = DataTrojan("what")
        compiler.push = DataTrojan("when")
        compiler.push = DataTrojan("where")
        compiler.push = DataTrojan("why")
        #Instantiate HomePage from page and pass from compiler through getter
        display = HomePage(compiler.pull)
        #Write loaded and compiled page from HomePage class function load()
        self.response.write(display.load())

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
