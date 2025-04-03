# This is a single-line comment
import os  # This is an inline comment

def foo():
    """This is a docstring"""
    print("Hello")  # Another inline comment

'''
This is a
multi-line comment using single quotes
'''

def bar():
    """
    This is a docstring
    with multiple lines
    """
    print("World")  # Inline with code

# ======= Mixed cases ======= #
x = 1  # x is 1
y = """This is not a comment"""  # But this is

"""
This looks like a multiline comment
but might be part of a string assignment
"""

z = '''
This could be confused
with a comment
'''  # Real comment here

# ======= Edge cases ======= #
print("Hello # World")  # String contains #
print('''Triple ' quotes''')  # String with triple quotes
print("""Triple \"\"\" quotes""")  # String with triple quotes

# ======= Last comment ======= #