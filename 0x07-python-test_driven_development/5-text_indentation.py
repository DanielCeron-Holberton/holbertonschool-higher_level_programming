#!/usr/bin/python3
"""Module to indent text"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    delimits = ".?:"
    new_text = text[:]
    for delim in delimits:
        token_list = new_text.split(delim)
        new_text = ""
        for token in token_list:
            token = token.strip(" ")
            if new_text == "":
                new_text = token + delim
            else:
                new_text += "\n\n" + token + delim
    print(new_text[:-3], end="")
