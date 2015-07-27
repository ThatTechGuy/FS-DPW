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
        #Instantiate library and data and configure compiler with data
        secure = DataTrojan()
        compiler = DataCompiler()
        compiler.config(secure.data)
        #With GETs we will give only the needed data to the compiler
        if self.request.GET['op']:
            compiler.collate(secure.auth(self.request.GET['op']))
            display = OperationPage(compiler.store)
        #Without GETS we will get only the compilers configuration
        else:
            display = LandingPage(compiler.store)
        #After everything is compiled, authorized, and collated we print
        self.response.write(display.load())

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
