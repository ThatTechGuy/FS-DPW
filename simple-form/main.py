'''
Name: Rick Martin
Class: DPW1507
Assignment: Simple Form
'''

import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        #Initializing an instance of Page class which will pass GET object
        form = Page(self.request.GET)
        #Calling load function to write to browser with instance initialized
        self.response.write(form.load())

#Declare Page and init with a sexy little optional param to avoid GET var errors on fresh load
class Page(object):
    def __init__(self, form=False):
        #All my html divied up into separate attributes and assign GET object
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
                <!--This guy here is because Python or GAEL apparently does not simply like to declare undefined GETs as False -->
                <input type="hidden" name="gender" value="" />
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
                <!--This guy here is because Python or GAEL apparently does not simply like to declare undefined GETs as False -->
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

    #Declare load function and run validate, assign error result then check
    def load(self):
        if self.form:
            self.form['error'] = self.validate()
            if self.form['error']:
                #We are here because we do have GET vars but also an error from validate
                output = self.header + self.error + self.survey + self.footer
            else:
                #Ended up here cuz we awesome sauce with no errors and GET vars
                output = self.header + self.success + self.footer
        else:
            #Made it this way cuz no GET or error, prob fresh page load
            output = self.header + self.survey + self.footer
        #This gimmick here returns our compilation and runs the string formatter through our GET vars (very handy)
        return output.format(**self.form)

    #Declare validate function and check to see if we have all the inputs, 4 or 5 is cool
    #UPDATE As of hidden input fix validate now requires strictly 5 or greater for success
    def validate(self):
        if len(self.form) > 5:
            if not self.form['game']:
                #This means we got all our inputs but the Game Selector was left at default
                result = "If your favorite game series is not listed, pick the one you can most tolerate."
            else:
                if not self.form['promo']:
                    #Could of had the hidden input take care of this but I wanted to use validate
                    self.form['promo'] = "did not enroll"
                result = False
        else:
            #We had less then 4 inputs, so go ahead and sling em back to the survey page
            result = "All fields are required, please complete the survey in its entirety and resubmit."
        return result

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
