from unittest import TestCase

import ddt

'''
Given an array nums and a value val, remove all instances of that value in-place and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Example 1:

Given nums = [3,2,2,3], val = 3,

Your function should return length = 2, with the first two elements of nums being 2.

It doesn't matter what you leave beyond the returned length.
Example 2:

Given nums = [0,1,2,2,3,0,4,2], val = 2,

Your function should return length = 5, with the first five elements of nums containing 0, 1, 3, 0, and 4.

Note that the order of those five elements can be arbitrary.

It doesn't matter what values are set beyond the returned length.
Clarification:

Confused why the returned value is an integer but your answer is an array?

Note that the input array is passed in by reference, which means modification to the input array will be known to the caller as well.

Internally you can think of this:

// nums is passed in by reference. (i.e., without making a copy)
int len = removeElement(nums, val);

// any modification to nums in your function would be known by the caller.
// using the length returned by your function, it prints the first len elements.
for (int i = 0; i < len; i++) {
    print(nums[i]);
}
'''

'''
[3,2,2,3],3-> [2,ij2,3,3]
[2,ij3],3

i=0, j=len(nums)-1
while i!=j
if j==t:
    j-=1
elif i!=t:
    i+=1
else:
    nums[i]=nums[j]
    nums[j]=t
return i

'''

class Solution(object):
    def removeElement(self, nums, val):
        if len(nums) == 1 and nums[0] == val:
            nums.pop()
            return []
        if not nums:
            return []
        i = 0
        j = len(nums) - 1
        while i <= j:
            if nums[j] == val:
                j -= 1
            elif nums[i] != val:
                i += 1
            else:
                nums[i] = nums[j]
                nums[j] = val
        return nums[0:j + 1]


@ddt.ddt
class LeetCodeTest(TestCase):

    def setUp(self):
        self.solution = Solution()

    @ddt.unpack
    @ddt.data(
        ([[0, 1, 2, 2, 3, 0, 4, 2], 2], [0, 1, 4, 0, 3]),
        ([[3, 2, 2, 3], 3], [2, 2]),
        ([[3, 2], 3], [2]),
        ([[3], 3], []),
        ([[3,3], 3], []),
    )
    def test_solution(self, args, output):
        response = self.solution.removeElement(*args)
        self.assertEqual(response, output, "\n\nexpected: {} \n actual: {}\n".format(output, response))
