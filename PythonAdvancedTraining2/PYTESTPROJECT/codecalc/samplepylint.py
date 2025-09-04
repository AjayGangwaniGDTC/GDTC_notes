# This is an example module for Pylint demonstration


X = 42 # C0103: constant name should be UPPER_CASE

def _foo(bar): # C0103: function name should be lowercase_with_underscores
    """does something weird""" # C0116: not capitalized
    result = bar + 1
    return result


def uppercase():
    print('SHOULD NOT BE CAPITALIZED')
    return None


def multiline():
    print("Bad formatting") # C0321: multiple statements on one line


def long_line_example():
    return "This is a very long string that should probably be broken into multiple lines because it exceeds the default line length which is set to 100 characters in PEP 8."


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hi(self):
        print(f"Hi, I'm {self.name} and I'm {self.age} years old.")

def main():
    _foo(5)
    uppercase()
    multiline()
    
if __name__ == "__main__":
    main()