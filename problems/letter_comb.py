from unittest import TestCase

import ddt

'''
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

("2", "abc")
("3", "def")
("4", "ghi")
("5", "jkl")
("6", "mno")
("7", "pqrs")
("8", "tuv")
("9", "wxyz")
    
Example:
Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
'''


class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        sol=[]

        def backtrack(candidate):
            if find_solution(candidate):
                sol.append(candidate)

            # iterate all possible candidates.
            for next_candidate in list_of_candidates:
                if is_valid(next_candidate):
                    # try this partial candidate solution
                    place(next_candidate)
                    # given the candidate, explore further.
                    backtrack(next_candidate)
                    # backtrack
                    remove(next_candidate)



@ddt.ddt
class LeetCodeTest(TestCase):

    def setUp(self):
        self.solution = Solution()

    @ddt.unpack
    @ddt.data(
        (["23"], ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]),
    )
    def test_solution(self, args, output):
        response = self.solution.letterCombinations(*args)
        self.assertEqual(response, output, "\n\nexpected: {} \n actual: {}\n".format(output, response))
