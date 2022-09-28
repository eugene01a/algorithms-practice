'''
Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
Note:

Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output: 5

Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.
Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: 0

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
'''

from collections import defaultdict, deque
from unittest import TestCase

import ddt
from nose.plugins.attrib import attr


class Solution(object):
    def __init__(self):
        self.length = 0
        # Dictionary to hold combination of words that can be formed,
        # from any given word. By changing one letter at a time.
        self.all_combo_dict = defaultdict(list)

    def visitWordNode(self, queue, visited, others_visited):
        current_word, level = queue.popleft()
        for i in range(self.length):

            # Intermediate words for current word
            intermediate_word = current_word[:i] + "*" + current_word[i + 1:]
            # Next states are all the words which share the same intermediate state.

            for word in self.all_combo_dict[intermediate_word]:

                # If the intermediate state/word has already been visited from the
                # other parallel traversal this means we have found the answer.
                if word in others_visited:
                    ans = level + others_visited[word]
                    return level + others_visited[word]
                if word not in visited:
                    # print('\t' * tabs + 'visited[{}]={}'.format(word, level+1))
                    # print('\t' * tabs + 'queue={}'.format(list(queue)))
                    # Save the level as the value of the dictionary, to save number of hops.
                    visited[word] = level + 1
                    queue.append((word, level + 1))
        return None

    def ladderLength(self, beginWord, endWord, wordList):

        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """

        if endWord not in wordList or not endWord or not beginWord or not wordList:
            print('endWord not in wordList or not endWord or not beginWord or not wordList')
            return 0
        tabs = 1
        # Since all words are of same length.
        self.length = len(beginWord)
        for word in wordList:
            tabs += 1
            print(tabs * '\t' + "word={}".format(word))
            for i in range(self.length):
                tabs += 1
                print(tabs * '\t' + "i={}".format(i))
                # Key is the generic word
                # Value is a list of words which have the same intermediate generic word.
                self.all_combo_dict[word[:i] + "*" + word[i + 1:]].append(word)
                print(tabs * '\t' + "all_combo_dict[{}]={}".format(word[:i] + "*" + word[i + 1:], word))
                tabs -= 1
            tabs -= 1

        from pprint import pprint
        pprint(dict(self.all_combo_dict))

        print("--------------------------------------------------\nQueues for birdirectional BFS\n")
        queue_begin = deque([(beginWord, 1)])  # BFS starting from beginWord
        queue_end = deque([(endWord, 1)])  # BFS starting from endWord

        # Visited to make sure we don't repeat processing same word
        visited_begin = {beginWord: 1}
        visited_end = {endWord: 1}
        ans = None

        # We do a birdirectional search starting one pointer from begin
        # word and one pointer from end word. Hopping one by one.

        while queue_begin and queue_end:

            tabs += 1
            print(tabs * '\t' + "--------------One hop from begin word")
            print(tabs * '\t' + "queue_begin={}".format(list(queue_begin)))
            #
            ans = self.visitWordNode(queue_begin, visited_begin, visited_end)
            print(tabs * '\t' + "visitWordNode({}, {}, {})".format(queue_begin, visited_begin, visited_end))
            if ans:
                return ans

            print(tabs * '\t' + "--------------One hop from end word")
            print(tabs * '\t' + "queue_end={}".format(list(queue_begin)))
            ans = self.visitWordNode(queue_end, visited_end, visited_begin)
            print(tabs * '\t' + "visitWordNode({}, {}, {})".format(list(queue_end), visited_end, visited_end))
            if ans:
                return ans
            tabs -= 1

        return 0


@ddt.ddt
@attr("BFS")
class LeetCodeTest(TestCase):

    def setUp(self):
        self.solution = Solution()

    @ddt.unpack
    @ddt.data(
        (["hit", "cog", ["hot", "dot", "dog", "log", "cog"]], 5),
        # (["lost", "miss", ["most", "mist", "miss", "lost", "fist", "fish"]], 4),
    )
    def test_solution(self, args, output):
        response = self.solution.ladderLength(*args)
        self.assertEqual(response, output, "\n\nexpected: {} \n actual: {}\n".format(output, response))
