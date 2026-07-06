# Response Generation
from datetime import datetime

def generate_custom_response(stm,user_input, intent):
    
    # Initialization
    topic = ''
    reply = ''

    # Fixed Command Matching followed by intent matching
    # Last Topic Recall
    if user_input == 'last topic':
        reply = stm["topic"]
        topic = "recall topic"

    # Last Question Recall
    elif user_input == 'last question':
        reply = stm["last_question"]
        topic = "recall question"

    # Last Reply Recall
    elif user_input == 'last reply':
        reply = stm["last_reply"]
        topic = "recall reply"
    
    # Last Message Count Recall
    elif user_input == 'last message count':
        reply = str(stm["message_count"])
        topic = "recall message count"

    # Clear Memory (while preserving the name)
    elif user_input == 'clear memory':
        name = stm["name"]
        stm.clear()
        stm["name"] = name
        stm["message_count"] = 0
        reply = "Memory Cleared"
        topic = "clear memory"

    # Introduction
    elif "what is your name" in user_input:
        reply = "My name is talktome, and I love lowercase letters."
        topic = "introduction"

    # Greetings
    elif 'how are you' in user_input:
        reply = "I am doing well, even though I don't have feelings :)"
        topic = "well wishes"

    # Farewell
    elif intent == "Farewell":
        return None

    # Mood
    elif intent == 'Mood':
        if stm.get("mood") is None:
            stm["mood"] = input("Chatbot: I do not know your mood. How are you feeling today? ").lower().strip()
            
        reply = f"You are feeling {stm['mood']} today!"
        topic = "Mood"

    # Salutation
    elif intent == 'Salutation':
        reply = f"Hello, {stm['name']}! How can I assist you today?"
        topic = "Salutation"

    # Thankful
    elif intent == 'Thankful':
        reply = "You are welcome! What else can I assist you with today?"
        topic = "Thankful"

    # Time
    elif intent == 'Time':
        reply = "The current system time is " + datetime.now().strftime("%Y_%m_%d-%H_%M_%S")
        topic = "Time"

    # Unclear
    else:
        reply = f"You said {user_input}, I am not sure I understand you."
        topic = "Unclear"


    # Custom Reply and Theme return
    response = {}
    response["topic"] = topic
    response["reply"] = reply
    return response