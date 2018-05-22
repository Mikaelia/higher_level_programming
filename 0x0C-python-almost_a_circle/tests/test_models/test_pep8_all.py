#!/usr/bin/python3
import os
import unittest

import pep8


class Pep8Test(unittest.TestCase):

    def test_pep8(self):
        style = pep8.StyleGuide()
        style.options.max_line_length = 80
        check = style.check_files(['./models/'])
        self.assertEqual(check.total_errors, 0, 'PEP8 style errors: %d' % check.total_errors)
