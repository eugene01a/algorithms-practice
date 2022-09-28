class Solution(object):
    def isPalondrome(self, x):
        '''
        :param x: int
        :return:
        '''
        if -1<x<10:
            return True



solution = Solution()
assert solution.isPalondrome(121) is True
assert solution.isPalondrome(-121) is False
assert solution.isPalondrome(10) is False
