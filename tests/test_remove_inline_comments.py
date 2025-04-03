import unittest
from scripts.remove_comments import remove_inline_comments

class TestRemoveInlineComments(unittest.TestCase):
    def test_basic_cases(self):
        self.assertEqual(remove_inline_comments("print('Hello')"), "print('Hello')")
        self.assertEqual(remove_inline_comments("x = 1 # comment"), "x = 1")
        self.assertIsNone(remove_inline_comments("# Full line comment"))
    
    def test_string_handling(self):
        self.assertEqual(remove_inline_comments('url = "http://example.com" # comment'), 
                        'url = "http://example.com"')
        self.assertEqual(remove_inline_comments("print('# not a comment')"), 
                        "print('# not a comment')")
    
    def test_edge_cases(self):
        self.assertEqual(remove_inline_comments(""), "")
        self.assertEqual(remove_inline_comments("   "), "")
        self.assertEqual(remove_inline_comments('a="\\"" # comment'), 'a="\\""')

if __name__ == '__main__':
    unittest.main()