## Simple chatbot program ##

import response_generation as rg
import logs

def main():

    # Short Term Memory (For immediate Context)
    stm = {}

    # Log File Path
    log_file_path = logs.generate_log_file()
    
    # Name Input
    name = input("Chatbot: Enter your name: ")
    print("Chatbot: " + f"Hello, {name}!")
    logs.write_logs("Chatbot: " + f"Hello, {name}!", log_file_path)
    
    stm["name"] = name
    stm["message_count"] = 2


    # Conversational Loop
    while True:

        # Input
        user_input = input(f"{stm['name']}: ").lower().strip()
        logs.write_logs(f"{stm['name']}: " + user_input, log_file_path)
        chatbot_reply = ""
        topic = ""

        response = rg.generate_custom_response(stm,user_input)

        if response is None:
            print("Chatbot: " + f"Goodbye, {stm['name']}!")
            logs.write_logs("Chatbot: " + f"Goodbye, {stm['name']}!", log_file_path)
            logs.final_log(log_file_path)
            break
        else:
            chatbot_reply = response["reply"]
            topic = response["topic"]

            if chatbot_reply != None:
                print("Chatbot: " + chatbot_reply)
                logs.write_logs("Chatbot: " + chatbot_reply, log_file_path)

        # Short Term Memory Value Updation
        stm["last_question"] = user_input
        stm["last_reply"] = chatbot_reply
        stm["topic"] = topic
        stm["message_count"] = stm["message_count"]+2

if __name__ == "__main__":
    main()