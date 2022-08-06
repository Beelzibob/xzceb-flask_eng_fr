import unittest
from translator import englishToFrench, frenchToEnglish

class TestEnglishToFrench(unittest.TestCase): 
    def test1(self):
        self.assertNotEqual(englishToFrench(""),"") #check for null input
    def test2(self):
        self.assertEqual(englishToFrench("Hello"),"Bonjour")

class TestFrenchToEnglish(unittest.TestCase): 
    def test1(self):
        self.assertNotEqual(frenchToEnglish(""),"") #check for null input
    def test2(self):
        self.assertEqual(frenchToEnglish("Bonjour"),"Hello")

unittest.main()