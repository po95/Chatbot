from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot import ChatBot

bot = ChatBot('Sourav')
bot.set_trainer(ChatterBotCorpusTrainer)

bot.train(
	"chatterbot.corpus.bangla"
)

while True:
	request = input('You: ')
	response = bot.get_response(request)
	print ('Bot: ',response)