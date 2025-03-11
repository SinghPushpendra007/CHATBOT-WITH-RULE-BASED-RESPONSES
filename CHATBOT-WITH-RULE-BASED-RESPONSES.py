import re
import random

def chatbot_response(user_input):
    responses = {
        r'hi|hello|hey': [
            "Hello! How can I assist you today?",
            "Hi there! What can I do for you?",
            "Hey! Need any help?"
        ],
        r'how are you': [
            "I'm just a bot, but I'm functioning perfectly! How about you?",
            "I'm here and ready to assist! What’s on your mind?"
        ],
        r'what is your name|who are you': [
            "I am a chatbot created to assist you! You can call me ChatBot.",
            "I'm your virtual assistant. How can I help you today?"
        ],
        r'bye|goodbye|see you': [
            "Goodbye! Have a great day!",
            "See you later! Feel free to return if you need more help.",
            "Bye! Take care!"
        ],
        r'what can you do': [
            "I can answer your questions, chat with you, and assist in various tasks. Give it a try!",
            "I'm here to provide information, chat, and help you with general queries."
        ],
        r'thank you|thanks': [
            "You're welcome! Happy to help!",
            "No problem! Let me know if you need anything else."
        ],
        r'how does ai work': [
            "AI works by processing data, learning from patterns, and making decisions based on algorithms and models.",
            "Artificial Intelligence mimics human intelligence using algorithms and large datasets."
        ],
        r'what is machine learning': [
            "Machine learning is a subset of AI that enables computers to learn from data and improve their performance without being explicitly programmed.",
            "Machine learning uses algorithms to identify patterns in data and make predictions or decisions."
        ],
        r'what is the capital of (\w+)': [
            "I'm not sure, but you can check on Google for the capital of {}!",
            "You might want to look that up online for the capital of {}!"
        ],
        r'how old are you': [
            "I'm just a digital being, so I don't age! But I'm always learning new things!",
            "I don't have an age, but I’m always up to date with the latest knowledge!"
        ],
        r'tell me a joke': [
            "Why don’t scientists trust atoms? Because they make up everything!",
            "Why did the scarecrow win an award? Because he was outstanding in his field!"
        ],
        r'what is python': [
            "Python is a popular programming language known for its simplicity and versatility.",
            "Python is a powerful programming language used in web development, data science, AI, and more."
        ],
        r'help': [
            "Sure! What do you need help with?",
            "I'm here to help! Please tell me your question."
        ],
        r'what is your favorite color': [
            "I don't have preferences, but I think blue is nice!",
            "As a bot, I don't see colors, but I hear green is calming!"
        ]
    }
    
    user_input = user_input.lower()
    for pattern, response_list in responses.items():
        match = re.search(pattern, user_input)
        if match:
            response = random.choice(response_list)
            # If the response contains a placeholder, fill it with the matched group
            if '{}' in response:
                return response.format(match.group(1))  # Fill in the captured group
            return response  # Return a random response found
    
    return "I'm sorry, I don't understand that. Can you rephrase?"

# Chat loop
print("ChatBot: Hello! Type 'exit' to end the chat.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("ChatBot: Goodbye! Have a great day!")
        break
    print("ChatBot:", chatbot_response(user_input))
