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
- [base.py](models/base.py): The Base class
	- `to_json_string` converts dictionary list to JSON string
	- `save_to_file` writes JSON string to a file
	- `from_json_string` returns the list represented by JSON string
	- `create` returns a class instance with attributes already set
	- `load_from_file` returns a list of instances from a file
- [square.py](models/square.py): A Square class
	- `update` returns instance with updated values
	- `__str__` returns string representation of instance
	- `display` returns visual output of class
	- `to_dictionary` returns dictionary representation of class

- [rectangle.py](models/rectangle.py): A Rectangle class
	- `update` returns instance with updated values
	- `__str__` returns string representation of instance
	- `display` returns visual output of class
	- `to_dictionary` returns dictionary representation of class

## Tests

- [test_rectangle.py](tests/test-models/test_rectangle.py): Rectangle class tests
- [test_square.py](tests/test-models/test_square.py): Square class tests
- [test_base.py](tests/test-models/test_base.py): Base class tests
- [test_pep8_all.py](tests/test-models/test_pep8_all.py): PEP8 validation tests
