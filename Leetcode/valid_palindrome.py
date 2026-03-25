class Solution(object):
    def isPalindrome(self, s):
        string = "".join(char for char in s if char.isalnum())
        rev = string.lower()[::-1]
        if string.lower() == rev:
            return True
        else: 
            return False