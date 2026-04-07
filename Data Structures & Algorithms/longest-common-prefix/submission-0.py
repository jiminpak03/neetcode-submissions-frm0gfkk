class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        
        sortList = sorted(strs)
        res = ''

        first, last = sortList[0], sortList[-1]

        for n in range(min(len(first), len(last))):
            if first[n] != last[n]:
                return res
            res += first[n]
        return res
