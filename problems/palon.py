class Solution(object):
    def longestPalindrome(self, s):
        strlen = len(s)
        if (strlen < 2 or s == s[::-1]):
            return s
        longest = s[0:1]
        current_length = 2
        while (current_length < len(s)):  # while current size != str size
            idx = 0
            needSkip = False
            while (idx < strlen - current_length + 1 and needSkip == False):  # while idx not at the end
                current_str = s[idx:idx + current_length]
                if (current_length > len(longest) + 2):
                    return longest
                if (current_str == current_str[::-1] and len(current_str) > len(longest)):
                    longest = current_str
                    current_length = len(longest)
                    needSkip = True
                    if (idx + current_length == strlen):
                        break
                idx += 1
            current_length += 1
        return longest


str1 = 'asdmadadam'
str2 = 'pwwkewtrep'
str3 = 'bbbabba'

Solution().palon(str1)
Solution().palon(str2)
Solution().palon(str3)
