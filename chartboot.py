def chatbot_response(user_input):
    # Convert input to lowercase to make the matching case-insensitivehw
    user_input = user_input.lower()

    # Predefined responses
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you today?"
    elif "how are you" in user_input:
        return "I'm just a chatbot, but I'm here to help you!"
    elif "what is your name" in user_input:
        return "I'm a simple chatbot created to assist you."
    elif "who are you" in user_input:
        return "I'm a simple chatbot developed by Gopal."
    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye! Have a great day!"
    else:
        return "I'm sorry, I don't understand that. Can you please rephrase?"

# Main loop to interact with the chatbot
if __name__ == "__main__":
    print("Welcome to the simple chatbot. Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if "bye" in user_input.lower():
            print("Chatbot: Goodbye! Have a great day!")
            break
        response = chatbot_response(user_input)
        print("Chatbot:",response)
