class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        non_duplicates = set(nums)
            
        return len(nums) != len(non_duplicates)
