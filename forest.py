# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 17:10:42 2022

@author: michal_romanowski
"""

from collections import Counter
from collections import deque
from structlinks import LinkedList

from tree import Node
from tree import LeafNode

class Forest():
    def __init__(self, text: str):
        letters_frequencies = Counter(text)
        # self.__trees = LinkedList.LinkedList([LeafNode(letter, letters_frequencies[letter]) for letter in letters_frequencies])
        # self.__trees = list([LeafNode(letter, letters_frequencies[letter]) for letter in letters_frequencies])
        self.__trees = deque([LeafNode(letter, letters_frequencies[letter]) for letter in letters_frequencies])
        
    def pop_min_frequency_tree(self) -> Node:
        min_frequency_tree = min(self.__trees)
        self.__trees.remove(min_frequency_tree)
        return min_frequency_tree
    
    def append(self, tree: Node):
        self.__trees.append(tree)
    
    def is_singe_tree(self) -> bool:
        return len(self.__trees) == 1