## Simple chatbot program ##
# Name
name = input("Enter your name: ")
print(f"Hello, {name}!")

# Conversational Loop
while True:
    user_input = input("Abhi: ")
    
    if user_input.lower() == 'bye' or user_input.lower() == 'goodbye':
        print(f"Goodbye, {name}!")
        break
    elif user_input.lower() == "what is your name":
        print("My name is talktome, and I love lowercase letters.")
    elif user_input.lower() == 'hello' or user_input.lower() == 'hi':
        print(f"Hello, {name}! How can I assist you today?")
    elif user_input.lower() == 'how are you':
        print("I am doing well, even though I don't have feelings :)")
    elif user_input.lower() == 'thanks' or user_input.lower() == 'thank you' or user_input.lower() == 'thankyou':
        print("You are welcome! What else can I assist you with today?")
    else:
        print(f"You said {user_input}, I am not sure I understand you.")