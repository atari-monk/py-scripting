import unittest
from scripts.remove_comments import remove_comments

class TestRemoveComments(unittest.TestCase):
    def test_no_comments(self):
        code = """import os
def foo():
    return 42"""
        self.assertEqual(remove_comments(code), code)

    def test_single_line_comment(self):
        code = """# This is a comment
import os
def foo():
    return 42"""
        expected = """import os
def foo():
    return 42"""
        self.assertEqual(remove_comments(code), expected)

    def test_multiline_comments(self):
        code = """# Comment 1
# Comment 2
import os
# Another comment
def foo():
    return 42"""
        expected = """import os
def foo():
    return 42"""
        self.assertEqual(remove_comments(code), expected)

    def test_empty_lines_with_comments(self):
        code = """# Comment 1

# Comment 2
import os

# Comment after empty line
def foo():
    return 42"""
        expected = """
import os

def foo():
    return 42"""
        self.assertEqual(remove_comments(code), expected)

    def test_comment_after_code(self):
        code = """import os  # This is an inline comment
def foo():
    return 42"""
        # The function does not handle inline comments, so this should remain unchanged
        expected = """import os  # This is an inline comment
def foo():
    return 42"""
        self.assertEqual(remove_comments(code), expected)

    def test_only_comments(self):
        code = """# Just a comment
# Another comment"""
        expected = ""
        self.assertEqual(remove_comments(code), expected)

    def test_empty_input(self):
        self.assertEqual(remove_comments(""), "")

    def test_whitespace_only_lines(self):
        code = """   
# Comment
import os
   """
        expected = """   
import os
   """
        self.assertEqual(remove_comments(code), expected)

if __name__ == '__main__':
    unittest.main()