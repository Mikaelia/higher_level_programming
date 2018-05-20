#!/usr/bin/python3
import json
"""Base class module"""
class Base():
    """Base class"""
    __nb_objects = 0
    def __init__(self, id=None):
        """Base class instance
        Args:
            id(int): public instance attribute
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns json representation of dict"""
        if not list_dictionaries or list_dictionaries is None:
            j = []
        else:
            j = json.dumps(list_dictionaries)
        return j

    @classmethod
    def save_to_file(cls, list_objs):
        """saves json string to file"""
        with open(cls.__name__+ '.json', mode='w', encoding='utf-8') as f:
            data = []
            if (list_objs):
                for obj in list_objs:
                    data.append(obj.to_dictionary())
                data = cls.to_json_string(data)
            f.write(data)

