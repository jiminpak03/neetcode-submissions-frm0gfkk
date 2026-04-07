class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        nextnum = 0
        maxcount = 0
        tempcount = 1
        for num in hashset:
            if num - 1 not in hashset:
                nextnum = num + 1
                while nextnum in hashset:
                    tempcount += 1
                    nextnum += 1
                maxcount = max(maxcount, tempcount)
                tempcount = 1

        return maxcount
                
