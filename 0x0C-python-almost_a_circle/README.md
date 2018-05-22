# 0x0C. Python - Almost a circle

---------------  
## A project on:
- Unit testing
- How to serialize and deserialize a Class with JSON
- How to write and read to a file with JSON
- *args and **kwargs, and how to use them
- How to handle named arguments in a function

## Requirements
- All  files are interpreted/compiled on Ubuntu 14.04 LTS using python3
- Code follows PEP 8 style

## Models
- [base.py](base.py): The base class
	- `to_json_string` converts dictionary list to JSON string
	- `save_to_file` writes JSON string to a file
	- `from_json_string` returns the list represented by JSON string
	- `create` returns a class instance with attributes already set
	- `load_from_file` returns a list of instances from a file
- [square.py](square.py): A square class
	- `update` returns instance with updated values
	- `__str__` returns string representation of instance
	- `display` returns visual output of class
	- `to_dictionary` returns dictionary representation of class

- [rectangle.py](rectangle.py): A square class
	- `update` returns instance with updated values
	- `__str__` returns string representation of instance
	- `display` returns visual output of class
	- `to_dictionary` returns dictionary representation of class

## Tests

- [test_rectangle.py](test_rectangle.py): Rectangle class tests
- [test_square.py](test_square.py): Square class tests
- [test_base.py](test_base.py): Base class tests
- [test_pep8_all.py](test_pep8_all.py): PEP8 validation tests
