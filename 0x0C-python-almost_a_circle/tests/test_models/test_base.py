#!/usr/bin/python3
import json
import unittest
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):

    #ID tests:
    @classmethod
    def setUpClass(cls):
        cls.b = Base()
        cls.b1 = Base(None)
        cls.b2 = Base()
        cls.b3 = Base()
        cls.b4 = Base(7)
        cls.b5 = Base()

    @classmethod
    def tearDownClass(cls):
        pass

    def test_is_instance(self):
        self.assertIsInstance(self.b, Base)

    def test_no_id(self):
        self.assertEqual(self.b1.id, 2)
        self.assertEqual(self.b2.id, 3)
        self.assertEqual(self.b3.id, 4)

    def test_given_id(self):
        self.assertEqual(self.b4.id, 7)
        self.assertEqual(self.b5.id, 5)

    def test_dict_to_json(self):
        s1 = Square(1, 2, 3)
        dictionary = s1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertEqual(type(json_dictionary), type("I'm a string"))
        json_dictionary = Base.to_json_string(None)
        self.assertEqual(json_dictionary, "[]")

    def test_save_to_file(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        dict_list =([r1.to_dictionary(), r2.to_dictionary()])
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as file:
            output = file.read()
            new = json.loads(output)
        self.assertTrue(new == dict_list)

        #if passed None parameter, return empty list:

        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            output = file.read()
            new = json.loads(output)
        self.assertTrue(new == []) #overwrites file

    def test_from_json_string(self):
        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertTrue(list_input == list_output)

        # if input empty, return an empty list
        list_input = None
        list_output = Rectangle.from_json_string(list_input)
        self.assertTrue([] == list_output)

    def test_create(self):
        r1 = Rectangle(3, 5, 1, 3)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertFalse(r1 is r2)
        self.assertFalse(r1 == r2)
        self.assertEqual(r2.width, 3)
        self.assertEqual(r2.height, 5)
        self.assertEqual(r2.x, 1)
        self.assertEqual(r2.y, 3)

    def test_load_from_file(self):

        #test rectangles

        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]
        inlist = [r1.__str__(), r2.__str__()]
        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()
        outlist = []
        for instance in list_rectangles_output:
            outlist.append(instance.__str__())
        self.assertEqual(outlist, inlist)

        #test non-existing file
        self.assertEqual(Square.load_from_file(), [])

if __name__ == '__main__':
    unittest.main()
