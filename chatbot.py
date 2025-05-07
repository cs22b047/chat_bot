from transformers import pipeline

# FAQ Data
faq_data = {
    "What are the specs of the latest smartphones?": "The latest smartphones come with 6.7-inch OLED displays, Snapdragon 8 Gen 3 processors, 12GB RAM, and 256GB storage.",
    "How can I track my order?": "You can track your order by going to our website and entering your order ID in the tracking section.",
    "What is your return policy?": "Our return policy allows for returns within 30 days of purchase with a valid receipt.",
    "What payment methods are available?": "We accept Credit cards, Debit Cards, UPI and Cash.",
    "What is the warranty information for products?": "All our products come with a 1-year manufacturer's warranty.",
}

# LLM Setup
chatbot = pipeline("text2text-generation", model="google/flan-t5-base")

# Store conversation history in a saperate file an load latest 10 conversations for context.
HISTORY_FILE = "conversation_history.txt"

# 4. Load last N exchanges from file
def load_recent_history(n=10):
    with open(HISTORY_FILE, "r") as file:
        lines = file.readlines()
        # Group every 2 lines as one exchange
        exchanges = [lines[i] + lines[i+1] for i in range(0, len(lines) - 1, 2)]
        return exchanges[-n:]

# Append new exchange to history file
def append_to_history(user, bot):
    with open(HISTORY_FILE, "a") as file:
        file.write(f"User: {user}\n")
        file.write(f"Chatbot: {bot}\n")

# Convert FAQ to string
def faq_to_string(faq):
    return "\n".join([f"{q} {a}" for q, a in faq.items()])

# Get response with history context
def get_response(query, history):
    faq_string = faq_to_string(faq_data)
    context = "".join(history)
    prompt = f"You are a chatbot designed to answer questions based on the following FAQ:\n\n{faq_string}\n\n" \
             f"Previous conversation:\n{context}\n\n" \
             f"User question: {query}\n" \
             f"Answer:"
    response = chatbot(prompt, max_length=200)[0]['generated_text']
    return response

print("Chatbot: Hello! How can I help you today?")
while True:
    user_input = input("User: ")
    if user_input.lower() == "exit":
        print("Chatbot: Bye!")
        break
    recent_history = load_recent_history(10)
    bot_response = get_response(user_input, recent_history)
    print("Chatbot:", bot_response)
    append_to_history(user_input, bot_response)
