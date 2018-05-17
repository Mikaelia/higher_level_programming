#!/usr/bin/python3
class Student():
    """A student class"""

    def __init__(self, first_name, last_name, age):
        """
            Initializes instance of Student class
            Args:
                first_name[str]: first name string
                last_name[str]: last name string
                age[int]: age of student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """returns dictionary representation of student instance"""
        dic = {}
        if attrs is None:
            return self.__dict__
        for attr in attrs:
            if attr in self.__dict__:
                dic[attr] = self.__dict__[attr]
        return dic

    def reload_from_json(self, json):
        """ Replaces all attributes of the Student instance:
            Args:
                json[dict]: dictionary that holds attributes
        """
        for key, value in json.items():
            self.__dict__[key] = value
