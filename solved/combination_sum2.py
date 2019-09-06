from unittest import TestCase

import ddt

'''
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]
'''


class Solution(object):

    def _combinationSum2(self, candidates, target):
        visited = set()
        sol = []

        def DFS(total, curr, neighbors):
            if total == target:
                sol.append(curr)
            if total < target:
                for i in range(len(neighbors)):
                    cand = curr + [neighbors[i]]
                    cand.sort()
                    im_cand = tuple(cand)
                    if im_cand not in visited:
                        visited.add(im_cand)
                        DFS(total + neighbors[i], cand, neighbors[:i] + neighbors[i + 1:])

        candidates.sort()
        while candidates[-1] >= target:
            if candidates[-1] == target:
                sol.append([candidates[-1]])
            candidates.pop()
        for i in range(len(candidates)):
            DFS(candidates[i], [candidates[i]], candidates[:i] + candidates[i + 1:])

        sol.sort()
        return sol

    tabs = 0
    def combinationSum2(self, candidates, target):
        def backtrack(start, end, tmp, target):
            print("{}backtrack({},{},{},{})".format(self.tabs*'\t', start, end, tmp, target))
            if target == 0:
                ans.append(tmp[:])
                print("{}ans={}".format(self.tabs*'\t', ans))
            elif target > 0:
                self.tabs +=1
                for i in range(start, end):
                    if i > start and candidates[i] == candidates[i - 1]:
                        continue
                    tmp.append(candidates[i])

                    backtrack(i + 1, end, tmp, target - candidates[i])
                    tmp.pop()
                self.tabs -= 1



        ans = []
        candidates.sort(reverse=True)
        print("candidates={}, target={}".format(candidates, target))
        print("backtrack(start, end, tmp, target)")
        backtrack(0, len(candidates), [], target)
        return ans


@ddt.ddt
class LeetCodeTest(TestCase):

    def setUp(self):
        self.solution = Solution()

    @ddt.unpack
    @ddt.data(
        ([[10, 1, 2, 7, 6, 1, 5], 8], [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]),
        ([[2, 5, 2, 1, 2], 5], [[1, 2, 2], [5]]),
    )
    def test_solution(self, args, output):
        response = self.solution.combinationSum2(*args)
        self.assertEqual(response, output, "\n\nexpected: {} \n actual: {}\n".format(output, response))
