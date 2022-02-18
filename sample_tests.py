import unittest

import random
import string

from main import Code
from tree import LeafNode, InnerNode


class SampleTests(unittest.TestCase):

    code = Code()

    def test_example_string(self):
        result = self.code.create_code("abacaca")
        self.assertEqual(result,
                         InnerNode(
                             InnerNode(
                                 LeafNode("b", 1),
                                 LeafNode("c", 2)
                             ),
                             LeafNode("a", 4)
                         ))

    def test_one_letter(self):
        result = self.code.create_code("aaaaa")
        self.assertEqual(result, LeafNode("a", 5))
    
    def test_uppercases_string(self): # depending on requirements different output could be expected
        result = self.code.create_code("abAcaCa")
        self.assertEqual(result,
                         InnerNode(
                             InnerNode(
                                 LeafNode("b", 1),
                                 LeafNode("c", 2)
                             ),
                             LeafNode("a", 4)
                         ))
        
    def test_special_chars_string(self):
        result = self.code.create_code("&_&*&*&") # depending on requirements different output could be expected
        self.assertEqual(result,
                         InnerNode(
                             InnerNode(
                                 LeafNode("_", 1),
                                 LeafNode("*", 2)
                             ),
                             LeafNode("&", 4)
                         ))
        
    def test_special_empty_string(self):
        result = self.code.create_code("")
        self.assertEqual(result, None)
        
    def test_deep_tree(self):
        result = self.code.create_code("abbccccddddd")
        self.assertEqual(result,
                         InnerNode(
                             LeafNode("d", 5),
                             InnerNode(
                                 InnerNode(
                                     LeafNode("a", 1), 
                                     LeafNode("b", 2)),
                                 LeafNode("c", 4))
                         ))
        
    def test_performance(self):
        random.seed(10)
        big_text = ''.join(random.choice(string.printable) for i in range(100000))
        
        self.code.create_code(big_text)
        # should add assertion for max time for it to be a real test
