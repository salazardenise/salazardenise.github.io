"""
ELIZA Chatbot Implementation

A simple implementation of the ELIZA chatbot, inspired by Joseph Weizenbaum's 
original 1966 program. This chatbot uses pattern matching and simple grammar 
transformation to generate responses.

The chatbot responds to user input by:
1. Matching input against predefined patterns
2. Transforming pronouns and verb forms
3. Generating appropriate responses based on matched patterns

Author: Denise Salazar
"""

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
    [r"I feel (.*)", ["Why do you feel {0}?", "Do you often feel {0}?"]],
    [r"(.*)I think(.*)", ["Do you really think so?", "But you are not sure you think so."]],
    [r"(.*)I know(.*)", ["Do you really know?", "But you are not sure you know."]],
    [r"(.*)hello(.*)", ["Hi there. Please state your problem."]],
    [r"(.*)name(.*)", ["Great, good to know.","I am not interested in names."]],
    [r"(.*)sorry(.*)", ["Please don't apologize.","Apologies are not necessary.","What feelings do you have when you apologize?"]],
    [r"(.*)", ["Tell me more!", "\\2"]],
]

def _reflect(fragment):
    """
    Transform pronouns and verb forms from first person to second person.
    
    This function converts the input from first person perspective to second person
    perspective by replacing pronouns and verb forms according to the grammar rules.
    For example, "I am happy" becomes "you are happy".
    
    Args:
        fragment (str): The text fragment to transform
        
    Returns:
        str: The transformed text with pronouns and verbs converted
    """
    tokens = fragment.lower().split()
    for i, token in enumerate(tokens):
        if token in grammar:
            tokens[i] = grammar[token]
    return ' '.join(tokens)

def _analyze(input_text):
    """
    Analyze input_text and generate an appropriate response.
    
    This function matches the input_text against predefined patterns and generates
    a response based on the first matching pattern. It uses regex matching to identify
    patterns and applies pronoun reflection to create more natural responses.
    
    Args:
        input_text (str): The input text to analyze
        
    Returns:
        str: A response string based on the matched pattern, or "I don't understand."
             if no pattern matches
    """
    for pattern, messages in rules:
        match = re.match(pattern, input_text.rstrip(".!"))
        if match:
            response = random.choice(messages)
            reflected = _reflect(match.group())
            return re.sub(r"\\2", reflected, response.format(match.group(1)))
    return "I don't understand."

def chatbot_response(input_text):
    """
    Main interface function for the ELIZA chatbot.
    
    This is the primary function that should be called to get a response from the
    ELIZA chatbot. It serves as a wrapper around the analyze function and provides
    a clean interface for external code to interact with the chatbot.
    
    Args:
        input_text (str): The input text
        
    Returns:
        str: The chatbot's response to the input_text
    """
    return _analyze(input_text)

if __name__ == "__main__":
    user_input = input("You: ")
    print("Bot: " + chatbot_response(user_input))
