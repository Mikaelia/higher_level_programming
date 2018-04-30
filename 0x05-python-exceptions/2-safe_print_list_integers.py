#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        l = 0
        for i in range(x):
            l += 1
            print("{:d}".format(my_list[i]), end="")
        print()
        return l
    except ValueError:
        print('', end='')
    except TypeError:
        print('', end='')
    except IndexError:
      print()
      return count
