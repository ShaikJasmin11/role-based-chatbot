import pickle
from utils import get_response

model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

print("Select role: teacher / fitness / hr")
role = input("Role: ").lower()

print("Chatbot started. Type 'exit' to stop.")

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break

    vec = vectorizer.transform([user_input])
    intent = model.predict(vec)[0]

    response = get_response(intent, role)
    print("Chatbot:", response)
