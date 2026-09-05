class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # create hashset
        # for every int, see if it's in the hashset
        # if no, add to the hashset
        # if yes, return true
        # return false

        hashset = set()

        for i in nums:
            if i in hashset:
                return True
            hashset.add(i)
        return False
