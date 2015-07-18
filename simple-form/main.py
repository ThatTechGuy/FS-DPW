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
        self.header = '''
        '''
        self.error = '''
        '''
        self.survey = '''
<form method="GET">
    <label>Your Name: </label>
    <input type="text" name="name" />
    </br>
    <label>Email Address: </label>
    <input type="email" name="email" />
    </br>
    <label>Your Gender: </label>
    <input type="radio" name="gender" value="Sir" /> Male
    <input type="radio" name="gender" value="Mam" /> Female
    </br>
    <label>Your Favorite Game: </label>
    <select name="game">
        <option value="0">Choose One...</option>
        <option value="Call of Duty">Call of Duty</option>
        <option value="Assassins Creed">Assassins Creed</option>
        <option value="Sly Cooper">Sly Cooper</option>
        <option value="Dance Dance Revolution">Dance Dance Revolution</option>
    </select>
    </br>
    <label>Receive Promotions? </label></br>
    <input type="checkbox" name="promo" value="1"> Yes, I would like to receive promotional emails.
</form>
        '''
        self.success = '''
        '''
        self.footer = '''
        '''

    def load(self):
        if self.form:
            error = validate()
        else:
            pass
        return output.format(**self.form)

    def validate(self):
        if self.form.len() >= 4:
            pass
        else:
            return "All fields are required, please complete the survey in its entirety and resubmit."


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
