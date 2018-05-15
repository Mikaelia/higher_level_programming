#!/usr/bin/python3
def inherits_from(obj, a_class):
    """Checks object is an instance of a class that inherited from specified class
    """
    return issubclass(obj.__class__, a_class) and obj.__class__ != a_class
