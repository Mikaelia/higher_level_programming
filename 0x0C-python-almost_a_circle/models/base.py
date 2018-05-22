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

    @staticmethod
    def from_json_string(json_string):
        """ returns the list of the JSON string representation `json_string`
            Args:
                json_string(str): String containing a list of dictionaries
            Returns:
                Empty list if json_string is empty/None, else list represented
        """
        if json_string:
            return json.loads(json_string)
        return []

    @classmethod
    def save_to_file(cls, list_objs):
        """saves json string to file"""
        with open(cls.__name__ + '.json', mode='w', encoding='utf-8') as f:
            data = []
            if (list_objs):
                for obj in list_objs:
                    data.append(obj.to_dictionary())
                data = cls.to_json_string(data)
                f.write(data)
            else:
                f.write('[]')

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set
            Args:
                dictionary: Double pointer to a dictionary
            Returns:
                An instance with all attributes set
        """
        from models.rectangle import Rectangle
        from models.square import Square

        if cls.__name__ == "Rectangle":
            r = Rectangle(1, 2)
        elif cls.__name__ == "Square":
            r = Square(5)
        r.update(**dictionary)
        return r

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        l = []
        try:
            with open(cls.__name__ + '.json', mode='r', encoding='utf-8') as f:
                json_list = json.dumps(json.load(f))
        except FileNotFoundError:
            return l
        list_dictionaries = cls.from_json_string(json_list)
        for d in list_dictionaries:
            l.append(cls.create(**d))
        return l
