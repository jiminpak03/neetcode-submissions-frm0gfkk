class Solution:
    def isAnagram(self, s: str, t: str):
        if len(s) != len(t):
            return False
        str1, str2 = [], []
        for c in s:
            str1.append(c)
        for c in t:
            str2.append(c)
    
        str1.sort() 
        str2.sort()

        if str1 != str2:
            return False
        return True
