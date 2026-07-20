from responses import responses
from preprocess import preprocess_text

def get_response(user_input):
    # Clean the user's input
    user_input = preprocess_text(user_input)

    # Check if the question exists
    if user_input in responses:
        return responses[user_input]

    # Default reply
    return "Sorry, I don't understand your question."