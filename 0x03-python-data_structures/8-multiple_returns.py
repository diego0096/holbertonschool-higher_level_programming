#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        tup = None
    else:
        tup = sentence[0]
    return len(sentence), tup
