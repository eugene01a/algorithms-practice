from unittest import TestCase

import ddt

'''
Design a HashSet without using any built-in hash table libraries.

To be specific, your design should include these functions:

add(value): Insert a value into the HashSet. 
contains(value) : Return whether the value exists in the HashSet or not.
remove(value): Remove a value in the HashSet. If the value does not exist in the HashSet, do nothing.

Example:

MyHashSet hashSet = new MyHashSet();
hashSet.add(1);         
hashSet.add(2);         
hashSet.contains(1);    // returns true
hashSet.contains(3);    // returns false (not found)
hashSet.add(2);          
hashSet.contains(2);    // returns true
hashSet.remove(2);          
hashSet.contains(2);    // returns false (already removed)
'''


class MyHashSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.values = []

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        if key not in self.values:
            self.values.append(key)

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        if key in self.values:
            self.values.remove(key)
        else:
            pass

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        return key in self.values


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)


class LeetCodeTest(TestCase):

    def setUp(self):
        self.solution = MyHashSet()

    def test_solution(self):
        self.solution.add(1)
        self.solution.add(2)
        self.assertTrue(self.solution.contains(1))
        self.assertFalse(self.solution.contains(3))
        self.solution.add(2)
        self.assertTrue(self.solution.contains(2))
        self.solution.remove(2)
        self.assertFalse(self.solution.contains(2))


