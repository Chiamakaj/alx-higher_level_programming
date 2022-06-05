#!/usr/bin/python3
def multiple_returns(sentence):
    count = len(sentence)
    if sentence == "":
        first_alph = "None"
    else:
        first_alph = sentence[0]
    return ((count, first_alph))
