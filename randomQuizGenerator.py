import random

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
   'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
   'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
   'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
   'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
   'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
   'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
   'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
   'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
   'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton','New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
   'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
   'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
   'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
   'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
   'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

for papernum in range(35):
    #creating question file and answerkey file
    quesp=open('Question File '+str(papernum+1),'a')
    answerpaper=open('Answer File '+str(papernum+1),'a')

    #creating header
    quesp.write('Question Paperc'+str(parenum+1))

    #creating questions and answers
    quesList=list(capitals.keys())
    random.shuffle(quesList)

    #writing into file
    for quesnum in range(50):
        state=quesList[quesnum]
        quesp.write(str(quesnum+1)+'= '+'What is the capital of '+state+"\n")
        correctAnswer=capitals[state]
        wrongAnswer=capitals.values()
        del wrongAnswer[wrongAnswer.index(correctAswer)]
        wrongoptions=random.sample(wrongAnswers,3)
        Answers=correctAnswer+wrongoptions
        random.shuffle(Answers)
        answerpaper.write('Answer of '+str(quesnum+1)+" = "+str(correctAnswer)w)
        for i in range(4):
            quesp.write(str(i)+": "+Answers[i]+"\n")
