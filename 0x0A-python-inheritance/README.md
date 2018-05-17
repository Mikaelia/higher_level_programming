# 0x0A. Python - Inheritance
  
## A project on:
- What is a superclass, baseclass or parentclass
- What is a subclass
- How to list all attributes and methods of a class or instance
- When can an instance have new attributes
- How to inherit class from another
- How to define a class with multiple base classes
- How to override a method or attribute inherited from the base class
- Which attributes or methods are available by heritage to subclasses
- What are, when and how to use `isinstance`, `issubclass`, `type` and `super` built-in functions

## Requirements
- All  files are interpreted/compiled on Ubuntu 14.04 LTS using python3
- Code follows PEP 8 style

## Tasks

- **[0-lookup.py](0-lookup.py)** - A function that returns the list of available attributes and methods of an object

- **[1-my_list.py](1-my_list.py)** - A class `MyList` that inherits from list:
- Public instance method: `def print_sorted(self)`: that prints the list, but sorted (ascending sort)

- **[2-is_same_class.py](2-is_same_class.py)** - A function that returns True if the object is exactly an instance of the specified class, else `False`.

- **[3-is_kind_of_class.py](3-is_kind_of_class.py)** - A function that returns `True` if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class, else `False`

- **[4-inherits_from.py](4-inherits_from.py)** - A function that returns `True` if the object is an instance of a class that inherited from specified class, else `False`.

- **[5-base_geometry.py](5-base_geometry.py)** - An empty class `BaseGeometry`

- **[7-base_geometry.py](7-base_geometry.py)** - `BaseGeometry` class 

- **[8-rectangle.py](8-rectangle.py)** - `Rectangle` class that inherits from `BaseGeometry`

- **[9-rectangle.py](9-rectangle.py)** - `Rectangle` that inherits from `BaseGeometry`

- **[10-square.py](10-square.py)** - `Square` that inherits from `Rectangle`

- **[11-square.py](11-square.py)** - `Square` that inherits from `Rectangle`
