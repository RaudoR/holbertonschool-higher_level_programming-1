#!/usr/bin/python3
def text_indentation(text):
    if type(text) is not str:
        raise TypeError("text must be a string")
    text = text.replace('.', '.\n')
    text = text.replace('?', '?\n')
    text = text.replace(':', ':\n')
    print("\n\n".join(list(l.strip() for l in text.split('\n'))), end="")
