'''
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
'''


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        chars=[]
        if len(s) == 1:
            return 0
        for i in range(0,len(s)):
            c=s[i]
            if c in chars:
                continue
            elif c not in s[:i] + s[i+1:]:
                return i
            else:
                chars.append(s[i])

        return -1

sol=Solution().firstUniqChar("aaaaddadadv")
print(sol)
sol=Solution().firstUniqChar("loveleetcode")
print(sol)
