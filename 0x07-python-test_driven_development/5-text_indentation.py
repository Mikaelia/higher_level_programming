#!/usr/bin/python3
def text_indentation(text):
    """
    A function that inserts two new lines after . ? and :

    Args:
        test(str): input string
    Raises:
        TypeError: if text is not a string
    """
    if type(text) is not str:
        raise TypeError('text must be a string')
    for i in range(len(text)):
        print(text[i], end='')
        if text[i] == '.' or text[i] == '?' or text[i] == ':':
            print()
            print()
