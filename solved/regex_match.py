class Solution(object):

    def isMatch(self, text, pattern):
        '''

        :param s: could be empty, contain lowercase a-z
        :param p: could be empty contain lowercase a-z and . or * assume valid regex
        :return:
        '''
        # bool(x) -> if x: return True else return False
        if not pattern:
            return not text

        first_match = bool(text) and pattern[0] in ['.', text[0]]

        # 2nd character in pattern is "*"
        if len(pattern) >= 2 and pattern[1] == '*':
            '''
            recursion with pattern incremented by 2, past the "*" returns True
            OR 
            first character matches AND recursion with text incremented by 1 character
            returns True
            '''
            return (self.isMatch(text, pattern[2:]) or
                    first_match and self.isMatch(text[1:], pattern))

        # 2nd character in pattern is not "*"
        else:
            '''
            recursion with both text and pattern incremented by 1 character returns True
            '''
            return first_match and self.isMatch(text[1:], pattern[1:])


print(Solution().isMatch("ac", ".*c"))
