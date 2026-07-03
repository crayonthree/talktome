## Simple chatbot program ##

# Response Generation
def generate_custom_response(stm,user_input):
    
    # Initialization
    topic = ''
    reply = ''

    # Logic
    # End
    if user_input == 'bye' or user_input == 'goodbye':
        return None

    # Mood
    elif user_input == 'what is my mood':
        if stm.get("mood") is None:
            reply = "I do not know your mood. How are you feeling today?"
            stm["mood"] = input(reply).lower().strip()
        else:
            reply = f"You are feeling {stm['mood']} today!"
        topic = "mood"

    # Last Topic Recall
    elif user_input == 'last topic':
        reply = stm["topic"]

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
        reply = stm["message_count"]
        topic = "recall message count"

    # Introduction
    elif user_input == "what is your name":
        reply = "My name is talktome, and I love lowercase letters."
        topic = "introduction"

    # Salutations
    elif user_input == 'hello' or user_input == 'hi':
        reply = f"Hello, {stm['name']}! How can I assist you today?"
        topic = "salutation"

    # Greetings
    elif user_input == 'how are you':
        reply = "I am doing well, even though I don't have feelings :)"
        topic = "well wishes"

    # Thankfulness
    elif user_input == 'thanks' or user_input == 'thank you' or user_input == 'thankyou':
        reply = "You are welcome! What else can I assist you with today?"
        topic = "thankfulness"

    # Unclear
    else:
        reply = f"You said {user_input}, I am not sure I understand you."
        topic = "unclear"


    # Custom Reply and Theme return
    response = {}
    response["topic"] = topic
    response["reply"] = reply
    return response

# Main
def main():

    # Short Term Memory (For immediate Context)
    stm = {}

    # Name Input
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

        response = generate_custom_response(stm,user_input)

        if response is None:
            print(f"Goodbye, {stm['name']}!")
            break
        else:
            chatbot_reply = response["reply"]
            topic = response["topic"]
            print(chatbot_reply)

        # Short Term Memory Value Updation
        stm["last_question"] = user_input
        stm["last_reply"] = chatbot_reply
        stm["topic"] = topic
        stm["message_count"] = stm["message_count"]+2

if __name__ == "__main__":
    main()