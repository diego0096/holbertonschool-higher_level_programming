#!/usr/bin/python3
'''
    see a text looking for a ? : or . to then print new lines.
    text (str) The string
'''


def text_indentation(text):
    abn = ""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for let in text:
        abn += let
        if let == "." or let == "?" or let == ":":
            while abn[0] == " ":
                abn = abn[1:]
            print(abn)
            print()
            abn = ""
    if len(abn) != 0:
        try:
            while abn[0] == " ":
                abn = abn[1:]
        except:
            pass
        print(abn, end="")
