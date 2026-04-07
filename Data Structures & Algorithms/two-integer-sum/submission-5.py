class Solution:
    def twoSum(self, nums: List[int], target: int):
        listMap = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in listMap:
                return [listMap[diff], i]
            listMap[n] = i