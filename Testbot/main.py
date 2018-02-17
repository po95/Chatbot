from chatterbot.trainers import ListTrainer # method to train the chatbot
from chatterbot import ChatBot # import the chatbot

bot = ChatBot('Test') #create a chatbot

conv = open('chateng.txt', 'r').readlines()

bot.set_trainer(ListTrainer) #set the trainers

bot.train(conv) # train the bot

while True:
	request = input('You: ')
	response = bot.get_response(request)
	print ('Bot: ', response)
	
	

