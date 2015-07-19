'''
Name: Rick Martin
Class: DPW1507
Assignment: Simple Form
'''

import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        form = Page(self.request.GET)
        self.response.write(form.load())

class Page(object):
    def __init__(self, form=False):
        self.form = form
        self.header = '''
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>GameSurveys</title>
        <link href="css/style.css" rel="stylesheet" type="text/css" />
    </head>
    <body>
        <header>
            <h2>GameSurveys</h2>
            <h3>Favorite Game Series Survey</h3>
        </header>
        '''
        self.error = '''
        <div id="error">{error}</div>
        '''
        self.survey = '''
        <div id="survey">
            <form method="GET">
                <label>Your Name: </label>
                <input type="text" name="name" />
                </br>
                <label>Email Address: </label>
                <input type="email" name="email" />
                </br>
                <label>Your Gender: </label>
                <input type="radio" name="gender" value="Mr." /> Male
                <input type="radio" name="gender" value="Ms." /> Female
                </br>
                <label>Favorite Game Series: </label>
                <select name="game">
                    <option value="">Choose One...</option>
                    <option value="Call of Duty">Call of Duty</option>
                    <option value="Assassins Creed">Assassins Creed</option>
                    <option value="Sly Cooper">Sly Cooper</option>
                    <option value="Dance Dance Revolution">Dance Dance Revolution</option>
                </select>
                </br>
                <label>Receive Promotions? </label></br>
                <input type="hidden" name="promo" value="" />
                <input type="checkbox" name="promo" value="enrolled"> Yes, I would like to receive promotional emails.
                </br>
                <input type="submit" value="Submit" />
            </form>
        </div>
        '''
        self.success = '''
        <div id="success">
            <h4>Thank You {gender} {name}! We received your submission...</h4>
            <p>As you requested, we <strong>{promo}</strong> you in our promotional newsletter in which we send out periodic updates on new surveys and more. However, for this survey we have recorded the following information from which you provided:
            <p>
            Your Email: <strong>{email}</strong></br>
            Favorite Game Series: <strong>{game}</strong>
            </p>
            <p>Again, Thank You!</br>
            <em>-GameSurveys</em></p>
        </div>
        '''
        self.footer = '''
        <div class="image">
            <img src="img/gamepad.png" />
        </div>
        <footer>
            <p>&copy; 2015 GameSurveys by Rick Martin</p>
        </footer>
    </body>
</html>
        '''

    def load(self):
        if self.form:
            self.form['error'] = self.validate()
            if self.form['error']:
                output = self.header + self.error + self.survey + self.footer
            else:
                output = self.header + self.success + self.footer
        else:
            output = self.header + self.survey + self.footer
        return output.format(**self.form)

    def validate(self):
        if len(self.form) >= 4:
            if not self.form['game']:
                result = "If your favorite game series is not listed, pick the one you can most tolerate."
            else:
                if not self.form['promo']:
                    self.form['promo'] = "did not enroll"
                result = False
        else:
            result = "All fields are required, please complete the survey in its entirety and resubmit."
        return result

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
