"""
Name: Rick Martin
Class: DPW1507
Assignment: Madlib
"""
#Opening Line in Program to Greet User
print "Welcome my friend, I am a fortune teller, answer my questions and I will tell you your future!"

#Initialize Array With All Initial Questions
questions = [
    "What is your favorite color? ",
    "What state do you live in? ",
    "Do you have any children? ",
    "How old were you in 1995? ",
    "How much wood does a wood chuck chuck? "
]

#Initialize Some Additional Dict/Array
madlib = {}
answers = []

#Define Function for Validating Certain Inputs
def validate():
    #Ensure we Have the Two Letter Abbreviation for State
    if len(answers[1]) > 2:
        answers[1] = raw_input("The two letter abbreviation for your state? ")
        validate()
    #Assign value to Kids for Later and Check for Valid Input
    if answers[2] == ("yes" or "y"):
        madlib['kids'] = raw_input("How many kids do you have? ")
    elif answers[2] == ("no" or "n"):
        madlib['kids'] = "0"
    else:
        answers[2] = raw_input("Seriously, do you have any kids? ")
        validate()

#Loop Through Each Question and Append to Our Answer Array
for question in questions:
    answer = raw_input(question).lower()
    answers.append(answer)

#Run Validation on All Answers We Currently Have
validate()

#Some Other Fun Stuff to Make This Interesting
if answers[0] == "red":
    madlib['mood'] = "angered"
elif answers[0] == "blue":
    madlib['mood'] = "saddened"
elif answers[0] == "green":
    madlib['mood'] = "envious"
elif answers[0] == "yellow":
    madlib['mood'] = "elated"
else:
    madlib['mood'] = "confused"

madlib['plate'] = answers[1].upper() + str(int(answers[3]) * int(madlib['kids']))


#Let's Print This Bad Boy Out and Laugh a Bit
print "You will meet someone soon, very soon indeed. They will be " + madlib['mood'] + " by the fact that you have " + madlib['kids'] + " kids. However you will be the best of friends as if you've known eachother since you were " + answers[3] + ". The first thing you will say to them when you meet is " + answers[4] + " and you will know it is who I speak of because their license plate will start with " + madlib['plate'] + "."
