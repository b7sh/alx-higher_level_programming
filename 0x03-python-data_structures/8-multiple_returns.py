#!/usr/bin/python3
def multiple_returns(sentence):
    returns_tuple = ()
    ln = len(sentence)
    if ln == 0:
        returns_tuple = None
    returns_tuple = ln, sentence[0]
    return returns_tuple
