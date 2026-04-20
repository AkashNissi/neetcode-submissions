class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dick = {}
      
        
        for i in range(len(nums)):
            dick[nums[i]] = i
        for i in range(len(nums)):
            if target - nums[i] in nums and i != dick[target - nums[i]]:
                return[i, dick[target - nums[i]]]