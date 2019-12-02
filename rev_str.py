class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        index = len(s)//2
        for i in range(index):
            j = len(s)-1-i
            temp = s[i]
            s[i] = s[j]
            s[j] = temp
