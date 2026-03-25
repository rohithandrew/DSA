class Solution(object):
    def romanToInt(self, s):
        symbols = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }
        x = 0
        a = list(s)
        for i in range(len(a) - 1):
            if symbols[a[i]] < symbols[a[i + 1]]:
                x -= symbols[a[i]]
            else:
                x += symbols[a[i]]
        x += symbols[a[-1]]
        return x