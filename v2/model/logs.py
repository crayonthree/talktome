from datetime import datetime

# Conversation Log File Creator
def generate_log_file():

    # Generating the file path
    date_time = datetime.now().strftime("%Y_%m_%d-%H_%M_%S")
    log_file_path = f"v2/logs/ConversationLog{date_time}"

    # Creating the file and adding initial text
    log_file = open(log_file_path,"x")
    with open(log_file_path, "a") as log_file:
        log_file.write("=== Conversation Started ===\n")
        log_file.write(datetime.now().strftime('%Y/%m/%d %H:%M:%S') + '\n\n')

    # Returning the file path for use
    return log_file_path

# Conversational Log Writer
def write_logs(message, log_file_path):

    # Adding Conversational Logs to the Log File
    with open(log_file_path, "a") as log_file:
        log_file.write("[" + datetime.now().strftime("%H:%M:%S") + "] " + message + '\n')

    return None

# End of Log
def final_log(log_file_path):

    # Adding Conversational Logs to the Log File
    with open(log_file_path, "a") as log_file:
        log_file.write("\n\n=== End of Conversation ===")

    return None