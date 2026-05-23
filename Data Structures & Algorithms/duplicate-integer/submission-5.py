class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        
        for i in nums:
            hashset.add(i)

        if len(hashset) == len(nums):
            return False

        else:
            return True
