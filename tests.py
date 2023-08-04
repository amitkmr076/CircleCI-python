import unittest
from main import say_hello, tell_joke

class TestMainFunctions(unittest.TestCase):

    def test_say_hello(self):
        greeting = say_hello()
        self.assertTrue(isinstance(greeting, str), "Greeting should be a string")

    def test_tell_joke(self):
        joke = tell_joke()
        self.assertTrue(isinstance(joke, str), "Joke should be a string")

if __name__ == "__main__":
    unittest.main()
