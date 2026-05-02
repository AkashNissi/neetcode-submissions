class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a = []
        for i in range(len(nums)):
            a.append(nums[i])
            if target - nums[i] in a and i != a.index(target - nums[i]):
                return [a.index(target - nums[i]), i]
        