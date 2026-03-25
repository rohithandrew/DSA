class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        a = strs[0]
        for i in range(len(strs)):
            while strs[i].find(a) != 0:
                a = a[:-1]
        return a