class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        uniqueNums = set(nums)
        if len(nums) > len(uniqueNums):
            return True
        return False