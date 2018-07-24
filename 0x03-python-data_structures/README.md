# 0x03. Python - Data Structures: Lists, Tuples
## About
An introductory project on:
- Lists, their methods, and how to use them
- How to use lists as stacks and queues
- List comprehensions and how to use them
- Tuples and how to use them
- Sequences
- Tuple packing
- Sequence unpacking
- The `del` statement and how to use it
## Requirements
### Python Scripts
- Python 3.4
- pep8 1.7
### C Files
- Ubuntu 14.04 LTS
- gcc 4.8.4 using the flags -Wall -Werror -Wextra and -pedantic
- [Betty Style](https://github.com/holbertonschool/Betty/wiki)
## File Descriptions
**[0-print_list_integer.py](0-print_list_integer.py)** - A function that prints all integers of a list.

**[1-element_at.py](1-element_at.py)** - A function that retrieves an element from a list like on C.

**[2-replace_in_list.py](2-replace_in_list.py)** - A function that replaces an element of a list at a specific position (like in C).

**[3-print_reversed_list_integer.py](3-print_reversed_list_integer.py)** - A function that prints all integers of a list, in reverse order.

**[4-new_in_list.py](4-new_in_list.py)** - A function that replaces an element in a list at a specific position without modifying the original list (like in C).

**[5-no_c.py](5-no_c.py)** - A function that removes all characters `c` and `C` from a string.
- You are not allowed to use `str.replace()`

**[6-print_matrix_integer.py](6-print_matrix_integer.py)** - Write a function that prints a matrix of integers.

**[7-add_tuple.py](7-add_tuple.py)** - A function that adds 2 tuples.
- Returns a tuple with 2 integers:
  - The first element should be the addition of the first element of each argument
  - The second element should be the addition of the second element of each argument
- You are not allowed to import any module
- You can assume that the two tuples will only contain integers
- If a tuple is smaller than 2, use the value 0 for each missing integer
- If a tuple is bigger than 2, use only the first 2 integers

**[8-multiple_returns.py](8-multiple_returns.py)** - A function that returns a tuple with the length of a string and its first character.

**[9-max_integer.py](9-max_integer.py)** - A function that finds the biggest integer of a list.
- You can assume that the list only contains integers
- You are not allowed to use the builtin `max()`

**[10-divisible_by_2.py](10-divisible_by_2.py)** - A function that finds all multiples of 2 in a list.
- Returns a new list with `True` or `False`, depending on wether the integer at the same position in the original list is a multiple of 2
- The new list should have the same size as the original list

**[11-delete_at.py](11-delete_at.py)** - A function that deletes the item at a specific position in a list.
- You are not allowed to use `pop()`

**[12-switch.py](12-switch.py)** - Completes the [source code](https://intranet.hbtn.io/rltoken/RfHRsVZK5IVZ5e4-0WAOJQ in order to switch value of `a` and `b`

