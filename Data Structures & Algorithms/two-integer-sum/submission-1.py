class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        indexMap = {}

        for i, n in enumerate(nums):
            if target - n in indexMap:
                return [indexMap[target - n], i]
            indexMap[n] = i