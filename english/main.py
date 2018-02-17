from chatterbot.trainers import ListTrainer # method to train the chatbot
from chatterbot import ChatBot # import the chatbot
import os

bot = ChatBot('Test') # create the chatbot
bot.set_trainer(ListTrainer) #set the trainers
for _file in os.listdir('files'):
	chats = open('files/' + _file, 'r').readlines()
	
	bot.train(chats)
	
	
while True:
	request = input('You: ')
	response = bot.get_response(request)
	
	print('Bot: '+ response)
	
 