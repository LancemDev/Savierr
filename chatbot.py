from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Create a chatbot instance
chatbot = ChatBot("SavingsBot")

# Train it with financial advice data
trainer = ListTrainer(chatbot)
trainer.train([
    "Here are some tips to save money on groceries: Plan your meals ahead, buy in bulk, and avoid impulse purchases.",
    "Consider setting up automatic transfers to your savings account to make saving effortless.",
    "Track your progress towards your savings goals to stay motivated!"
])

# Start a conversation
while True:
    user_input = input("You: ")
    response = chatbot.get_response(user_input)
    print("Bot:", response)
