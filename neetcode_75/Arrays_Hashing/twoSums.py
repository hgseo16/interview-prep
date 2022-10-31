from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashMap = defaultdict(int)    
        
        for index, num in enumerate(nums):
            diff = target - num
            if diff in hashMap:
                return [hashMap[diff], index]
            else:
                hashMap[num] = index
