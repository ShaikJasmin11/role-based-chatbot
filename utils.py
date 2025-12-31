def get_response(intent, role):
    responses = {
        "teacher": {
            "greeting": "Hello! I’m your teacher. What would you like to learn today?",
            "teaching": "Sure! Let’s break it down step by step.",
            "thanks": "You’re welcome. Keep learning!",
            "goodbye": "Goodbye! Revise regularly.",
        },
        "fitness": {
            "greeting": "Hey! Ready to crush your fitness goals?",
            "fitness": "Consistency is key. Focus on diet and training.",
            "thanks": "Anytime! Stay strong 💪",
            "goodbye": "See you! Don’t skip leg day.",
        },
        "hr": {
            "greeting": "Hello. How may I assist you today?",
            "hr": "Please refer to company policies for accurate details.",
            "thanks": "Happy to help.",
            "goodbye": "Have a great day.",
        }
    }

    return responses.get(role, {}).get(
        intent, "Can you please clarify your request?"
    )
