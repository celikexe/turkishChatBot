import os
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer
from django.http import JsonResponse
from myproject.settings import BASE_DIR
training_data_dir = os.path.join(BASE_DIR, 'myapp', 'data', 'training_data')
from myapp.models import Conversation
training_data = []
for filename in os.listdir(training_data_dir):
    filepath = os.path.join(training_data_dir, filename)
    if os.path.isfile(filepath):
        with open(filepath) as f:
            lines = f.readlines()
            training_data += lines

# veri kümesi ekle
conversations = [
    'Merhaba',
    'Merhaba, nasılsın?',
    'İyiyim, teşekkür ederim. Sen?',
    'Ben de iyiyim, teşekkür ederim.',
    'Ne yapıyorsun?',
    'Seninle sohbet ediyorum. :)'
]

chatbot = ChatBot('Chat Bot')
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("myapp/data/turkish/conversations.yml")
trainer = ListTrainer(chatbot)

training_data_file = 'myapp/data/training_data'
with open(training_data_file) as f:
    training_data = f.readlines()

trainer.train(training_data)

def get_bot_response(message):
    response = chatbot.get_response(message)
    return str(response)

def get_response(request):
    user_input = request.GET.get('msg')
    response = chatbot.get_response(user_input)
    Conversation.objects.create(user_input=user_input, bot_response=str(response))
    return JsonResponse({'response': str(response)})

def train_bot():
    trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("data.training_data")
print("Chat bot trained successfully!")