import unittest
from remove_comments import remove_inline_comments

class TestRemoveInlineComments(unittest.TestCase):

    def test_no_comment(self):
        self.assertEqual(remove_inline_comments("print('Hello')"), "print('Hello')")
    
    def test_inline_comment(self):
        self.assertEqual(remove_inline_comments("print('Hello') # greeting"), "print('Hello')")
    
    def test_whole_line_comment(self):
        self.assertIsNone(remove_inline_comments("# This is a comment"))
    
    def test_whitespace_before_comment(self):
        self.assertIsNone(remove_inline_comments("   # Indented comment"))
    
    def test_comment_in_string(self):
        self.assertEqual(remove_inline_comments('print("# not a comment")'), 'print("# not a comment")')
    
    def test_escaped_quote_in_string(self):
        self.assertEqual(remove_inline_comments('print("\\" # not a comment") # real comment'), 
                         'print("\\" # not a comment")')
    
    def test_multiple_strings(self):
        self.assertEqual(remove_inline_comments('a="x # 1"; b=\'y # 2\'; c=z # 3'), 
                         'a="x # 1"; b=\'y # 2\'; c=z')
    
    def test_empty_line(self):
        self.assertEqual(remove_inline_comments(""), "")
    
    def test_only_whitespace(self):
        self.assertEqual(remove_inline_comments("   \t  "), "")
    
    def test_comment_after_string(self):
        self.assertEqual(remove_inline_comments('"string" # comment'), '"string"')
    
    def test_multiple_hashes_outside_string(self):
        self.assertEqual(remove_inline_comments('a=1 ## value # comment'), 'a=1')
    
    def test_triple_quoted_string(self):
        # Note: The current function doesn't fully handle triple-quoted strings
        self.assertEqual(remove_inline_comments('"""multi\nline""" # comment'), '"""multi\nline"""')

if __name__ == '__main__':
    unittest.main()