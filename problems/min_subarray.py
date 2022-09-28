from unittest import TestCase

import ddt

'''
Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum >= s. If there isn't one, return 0 instead.

Example: 

Input: s = 7, nums = [2,3,4,i2,j1,3] sum=6, lens=[2]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.
Follow up:
If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n). 

lens=[len(nums)]
i,j=0,0
#i=start of sub
#j=end of sub
sum=0
while i,j<len(nums):
    if sum+nums[j]<s:
        sum+=nums[j]
        j+=1
    elif sum+nums[j]>s:
        i+=1
        sum=nums[i]
    else:
        #sum+nums[j]==s
        lens.append(j-i+1)
        sum=0
        i=j+1
        j=i+1
        
if min: 
    return min(lens)
else:
 return 0
'''


class Solution(object):
    def minSubArrayLen(self, s, nums):
        if not nums:
            return 0
        if s in nums:
            return 1

        i = 0
        sum = 0
        while sum < s and i < len(nums):
            sum += nums[i]
            i += 1
        print "sum={}".format(sum)
        if sum < s:
            return 0
        else:
            i -= 1

        sol = i

        j = i
        i = 0
        add_j = False
        print "nums={}".format(nums)
        print "i={}, j={}, sum{}={}".format(i, j, nums[i:j + 1], sum)
        while i < j < len(nums):
            if add_j:
                sum += nums[j]
                add_j = False
            print "i={}, j={}, sum{}={}".format(i, j, nums[i:j + 1], sum)
            if j - i == sol:
                if sum < s:
                    sum -= nums[i]
                    i += 1
                    j += 1
                    add_j = True
                else:
                    # sum >=s
                    sum -= nums[j]
                    j -= 1
            elif j - i < sol:
                if sum < s:
                    sum -= nums[i]
                    i += 1
                    if j < len(nums) - 1:
                        j += 1
                        add_j = True
                else:
                    # sum >=s
                    sol = j - i
                    sum -= nums[i]
                    i += 1
                    if j < len(nums) - 1:
                        j += 1
                        add_j = True

            else:
                print i, j, sol, sum
                # j-i > sol should never reach here
                raise Exception
        return sol + 1


@ddt.ddt
class LeetCodeTest(TestCase):

    def setUp(self):
        self.solution = Solution()

    @ddt.unpack
    @ddt.data(
        ([7, [2, 3, 4, 2, 1, 3]], 2),
        ([7, [2, 3, 1, 2, 4, 3]], 2),
        ([11, [1, 2, 3, 4, 5]], 3),
        ([3, [1, 1]], 0),
        ([6, [10, 2, 3]], 1),
        ([9, [9, 4, 9, 8, 4]], 1),
        ([4, [1, 4, 4]], 1),
    )
    def test_solution(self, args, output):
        response = self.solution.minSubArrayLen(*args)
        self.assertEqual(response, output, "expected: {} \n actual: {}\n".format(output, response))
