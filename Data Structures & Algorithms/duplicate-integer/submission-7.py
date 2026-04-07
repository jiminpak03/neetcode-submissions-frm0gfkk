class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        while nums:
            key = nums[0]
            nums.remove(nums[0])
            if key in nums:
                return True
        return False
