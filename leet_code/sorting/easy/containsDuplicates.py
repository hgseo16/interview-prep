class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        sorted = nums.sort()
        count = 0
        for i in range(1, len(nums)):
            if nums[count] == nums[i]: return True
            count += 1
            
        return False
        
