#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    if sentence:
        return (length, sentence[0])
    else:
        return (0, None)
