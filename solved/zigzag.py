"""

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
PAYPALISHIRIN

And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I



"""

'''
MY SOLUTION
'''
class Solution():
    def convert(self, s, numRows):

        if numRows >= len(s) or numRows == 1:
            return s
        elif numRows < 1:
            return ''
        else:
            idx = 0
            row = 0
            ans_rows = [''] * numRows
            reverse = False
            while idx < len(s):

                ans_rows[row] += s[idx]

                if row == numRows - 1:
                    reverse = True
                if row == 0:
                    reverse = False
                idx += 1
                if reverse:
                    row -= 1
                else:
                    row += 1

        ans = ''.join(ans_rows)
        return ans


ans = Solution().zigzag("PAYPALISHIRING", 3)
print(ans)
