## Simple chatbot program ##

# Short Term Memory (For immediate Context)
stm = {}

# Name
name = input("Enter your name: ")
print(f"Hello, {name}!")
stm["name"] = name
stm["message_count"] = 2

# Conversational Loop
while True:

    # Input
    user_input = input("Abhi: ").lower().strip()
    chatbot_reply = ""
    topic = ""

    # End
    if user_input == 'bye' or user_input == 'goodbye':
        print(f"Goodbye, {name}!")
        break

    # Mood
    elif user_input == 'what is my mood':
        if stm.get("mood") is None:
            chatbot_reply = "I do not know your mood. How are you feeling today?"
            stm["mood"] = input(chatbot_reply).lower().strip()
        else:
            chatbot_reply = f"You are feeling {stm["mood"]} today!"
            print(chatbot_reply)
        topic = "mood"

    # Last Topic Recall
    elif user_input == 'last topic':
        chatbot_reply = stm["topic"]
        print(chatbot_reply)

    # Last Question Recall
    elif user_input == 'last question':
        chatbot_reply = stm["last_question"]
        print(chatbot_reply)
        topic = "recall question"

    # Last Reply Recall
    elif user_input == 'last reply':
        chatbot_reply = stm["last_reply"]
        print(chatbot_reply)
        topic = "recall reply"
    
    # Last Message Count Recall
    elif user_input == 'last message count':
        chatbot_reply = stm["message_count"]
        print(chatbot_reply)
        topic = "recall message count"

    # Introduction
    elif user_input == "what is your name":
        chatbot_reply = "My name is talktome, and I love lowercase letters."
        print(chatbot_reply)
        topic = "introduction"

    # Salutations
    elif user_input == 'hello' or user_input == 'hi':
        chatbot_reply = f"Hello, {name}! How can I assist you today?"
        print(chatbot_reply)
        topic = "salutation"

    # Greetings
    elif user_input == 'how are you':
        chatbot_reply = "I am doing well, even though I don't have feelings :)"
        print(chatbot_reply)
        topic = "well wishes"

    # Thankfulness
    elif user_input == 'thanks' or user_input == 'thank you' or user_input == 'thankyou':
        chatbot_reply = "You are welcome! What else can I assist you with today?"
        print(chatbot_reply)
        topic = "thankfulness"

    # Unclear
    else:
        chatbot_reply = f"You said {user_input}, I am not sure I understand you."
        print(chatbot_reply)
        topic = "unclear"

    # Short Term Memory Value Updation
    stm["last_question"] = user_input
    stm["last_reply"] = chatbot_reply
    stm["topic"] = topic
    stm["message_count"] = stm["message_count"]+2