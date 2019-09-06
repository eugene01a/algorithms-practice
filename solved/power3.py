# Returns true if n is power of 3, else false
def check(n):
    """ The maximum power of 3 value that
       integer can hold is 1162261467 ( 3^19 ) ."""
    return 1162261467 % n == 0


zx = [
    '(((())))',
    '((()()))',
    '((())())',
    '((()))()',
    '(()(()))',
    '(()()())',
    '(()())()',
    '(())(())',
    '(())()()',
]
