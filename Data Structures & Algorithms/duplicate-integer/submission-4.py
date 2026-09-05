class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # bruteforce: sorting nums, nested for loop to find if i = i + 1

        # create hashset
        # add nums to hashset
        # if nums value is int hashset -> true
        # return false

        seen = set()

        for i in nums:
            if i in seen:
                return True
            seen.add(i)
        return False