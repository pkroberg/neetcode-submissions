class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # bruteforce --> sort nums, nested if statements comparing i and i + 1 = O(n)^2

        # create hashmap {value : index}
        # iterate through nums
            # if target - nums[i] is in hashmap -> return indexes
            # add value and index to hashmap

        hashmap = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in hashmap:
                return [hashmap[diff], i]
            hashmap[n] = i