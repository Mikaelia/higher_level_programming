#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
    """
        A function that prints "My name is", followed by first and last names

        Args:
            first_name (str): First name string
            last_name (str): Last name string
    """
    if type(first_name) is not str:
        raise TypeError('first_name must be a string')
    if type(last_name) is not str:
        raise TypeError('last_name must be a string')
    print("My name is {} {}".format(first_name, last_name))
