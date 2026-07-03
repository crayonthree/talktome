## Simple chatbot program ##
# Name
name = input("Enter your name: ")
print(f"Hello, {name}!")

# Conversational Loop
while True:
    user_input = input("Abhi: ")
    
    if user_input.lower() == 'exit':
        print(f"Goodbye, {name}!")
        break
    
    print(f"You said: {user_input}")