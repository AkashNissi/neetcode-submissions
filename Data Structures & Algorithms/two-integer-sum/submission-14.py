class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashe = {}
        for i, val in enumerate(nums):
            if target - val in hashe:
                return [hashe[target-val], i]

            hashe[val] = i
        
        




