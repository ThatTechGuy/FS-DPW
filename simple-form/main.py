'''
Name: Rick Martin
Class: DPW1507
Assignment: Simple Form
'''

import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        form = Page()
        self.response.write(form.load(self.request.GET))

class Page(object):
    def __init__(self, form=False):
        self.form = form

    def load(self):
        if self.form:
            pass
        else:
            pass

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
