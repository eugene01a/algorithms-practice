from unittest import TestCase

'''
Design a HashMap without using any built-in hash table libraries.

To be specific, your design should include these functions:

put(key, value) : Insert a (key, value) pair into the HashMap. If the value already exists in the HashMap, update the value.
get(key): Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
remove(key) : Remove the mapping for the value key if this map contains the mapping for the key.

Example:

MyHashMap hashMap = new MyHashMap();
hashMap.put(1, 1);          
hashMap.put(2, 2);         
hashMap.get(1);            // returns 1
hashMap.get(3);            // returns -1 (not found)
hashMap.put(2, 1);          // update the existing value
hashMap.get(2);            // returns 1 
hashMap.remove(2);          // remove the mapping for 2
hashMap.get(2);            // returns -1 (not found) 

Note:

All keys and values will be in the range of [0, 1000000].
The number of operations will be in the range of [1, 10000].
Please do not use the built-in HashMap library.'''


class MyHashMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hashmap = {}

    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: None
        """
        self.hashmap[key] = value

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        if key in self.hashmap.keys():
            return self.hashmap[key]
        else:
            return -1

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: None
        """
        if key in self.hashmap.keys():
            del self.hashmap[key]
        else:
            pass


class LeetCodeTest(TestCase):

    def setUp(self):
        self.solution = MyHashMap()

    def test_solution(self):
        self.solution.put(1, 1)
        self.solution.put(2, 2)
        self.assertEqual(self.solution.get(1), 1)
        self.assertEqual(self.solution.get(3), -1)
        self.solution.put(2, 1)
        self.assertEqual(self.solution.get(2), 1)
        self.solution.remove(2)
        self.assertEqual(self.solution.get(2), -1)
