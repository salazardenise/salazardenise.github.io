import re
import random

grammar = {
    "am": "are",
    "was": "were",
    "i": "you",
    "i'd": "you would",
    "i've": "you have",
    "i'll": "you will",
    "my": "your",
    "are": "am",
    "you've": "I have",
    "you'll": "I will",
    "your": "my",
    "yours": "mine",
    "you": "me",
    "me": "you",
}

rules = [
    ["(.*)I think(.*)", ["Do you really think so?", "But you are not sure you think so."]],
    ["(.*)I know(.*)", ["Do you really know?", "But you are not sure you know."]],
    ["(.*)hello(.*)", ["Hi there. Please state your problem."]],
    ["(.*)name(.*)", ["Great, good to know.","I am not interested in names."]],
    ["(.*)sorry(.*)", ["Please don't apologize.","Apologies are not necessary.","What feelings do you have when you apologize?"]],
    ["(.*)", ["Tell me more!", "\\2"]],
]

def reflect(fragment):
    tokens = fragment.lower().split()
    for i, token in enumerate(tokens):
        if token in grammar:
            tokens[i] = grammar[token]
    return ' '.join(tokens)

def analyze(user_input):
    for pattern, messages in rules:
        match = re.match(pattern, user_input.rstrip(".!"))
        if match:
            response = random.choice(messages)
            reflected = reflect(match.group())
            return re.sub(r"\\2", reflected, response)
    return "I don't understand."

def chatbot_response(user_input):
    return analyze(user_input)

if __name__ == "__main__":
    user_input = input("You: ")
    print("Bot: " + chatbot_response(user_input))
    