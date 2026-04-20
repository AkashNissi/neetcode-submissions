class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for i, x in enumerate(nums):
            difference = target - x
            if difference in hashMap:
                return [hashMap[difference], i]
            hashMap[x] = i

