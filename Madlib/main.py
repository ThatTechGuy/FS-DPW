"""
Name: Rick Martin
Class: DPW1507
Assignment: Madlib
"""

print "Welcome my friend, I am a fortune teller, answer my questions and I will tell you your future!"

questions = [
    "What is your favorite color? ",
    "What state do you live in? ",
    "Do you have any children? ",
    "How old where you in 1990? ",
    "How much does a wood chuck chuck? "
]

madlib = {}
answers = []

def validate():
    if answers[0] == "red":
        madlib['mood'] = "angered"
    elif answers[0] == "blue":
        madlib['mood'] = "saddened"
    elif answers[0] == "green":
        madlib['mood'] = "envious"
    elif answers[0] == "yellow":
        madlib['mood'] == "elated"
    else:
        madlib['mood'] == "confused"
    if answers[2] == "yes" or "y":
        madlib['kids'] == raw_input("How many kids do you have? ")
    elif answers[2] == "no" or "n":
        madlib['kids'] == "no"
    else:
        answers[2] == raw_input("Seriously, do you have any kids? ")
        validate()

for question in questions:
    answer = raw_input(question).lower()
    answers.append(answer)
    validate()
