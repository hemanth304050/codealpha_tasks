def chatbot_reply(message):
    message = message.lower()

    if message == "hello":
        return "Hi!"
    elif message == "hi":
        return "Hello!"
    elif message == "how are you":
        return "I'm fine, thanks!"
    elif message == "bye":
        return "Goodbye!"
    else:
        return "Sorry, I didn't understand that."

def main():
    print("Simple Rule-Based Chatbot")
    print("Type 'bye' to exit.\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "bye":
            print("Chatbot: Goodbye!")
            break

        response = chatbot_reply(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    main()
