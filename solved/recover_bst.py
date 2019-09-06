from unittest import TestCase

import ddt

'''
PROBLEM
'''


class Solution(object):
    def combinationSum(self, candidates, target):
        sols = []
        visited = set()

        def DFS(comb_sum, comb, next_cands):
            if comb_sum == target:
                visited_comb = tuple(comb)
                if visited_comb not in visited:
                    sols.append(comb)
                    visited.add(visited_comb)


            else:
                i=0
                while i < len(next_cands):
                    if next_cands[i] + comb_sum > target:
                        next_cands.pop(i)
                    else:
                        comb_sum += next_cands[i]
                        comb.append(next_cands[i])
                        DFS(comb_sum, comb, next_cands)
                    i+=1

        i = 0
        while i<len(candidates):
            if candidates[i] == target:
                sols.append([candidates[i]])
            else:
                DFS(candidates[i], [candidates[i]], candidates)
            i+=1
        return sols


@ddt.ddt
class LeetCodeTest(TestCase):

    def setUp(self):
        self.solution = Solution()

    @ddt.unpack
    @ddt.data(
        ([[2, 3, 5], 8], [[2, 2, 2, 2], [2, 3, 3], [3, 5]]),
    )
    def test_solution(self, args, output):
        response = self.solution.combinationSum(*args)
        self.assertEqual(response, output, "\n\nexpected: {} \n actual: {}\n".format(output, response))
