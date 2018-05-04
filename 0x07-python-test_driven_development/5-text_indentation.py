#!/usr/bin/python3
def text_indentation(text):
    """
    A function that inserts two new lines after . ? and :

    Args:
        test(str): input string
    Raises:
        TypeError: if text is not a string
    """
    symbol = False
    if type(text) is not str:
        raise TypeError('text must be a string')
    for i, v in enumerate(text):
        if v == ' ' and symbol == True:
            pass
        else:
            symbol = False
        if symbol == False:
            print(v, end='')
        if v in '.?:':
            print('\n')
            symbol = True
