class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        else:
            y = str(x)
            rev = y[::-1]
            if y == rev:
                return True
            else:
                return False