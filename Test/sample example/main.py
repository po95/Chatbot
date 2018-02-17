#if you code in python 2.7 then must add coding: utf-8

from chatterbot import ChatBot

#create a new chat bot named charlie
chatbot = ChatBot(
	'Charlie',
	trainer = 'chatterbot.trainers.ListTrainer'
)

chatbot.train([
	"Hi, can I help you?",
	"Sure, I'd like to book a flight to Iceland",
	"Your flight has been booked."
])

#get a response to the input text "how are you "

response = chatbot.get_response('I would like to book a flight')

print (response)
