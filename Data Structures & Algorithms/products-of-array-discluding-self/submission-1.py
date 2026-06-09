class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        x = 1
        y = 1
        z = 0
        for i in nums:
            x *= i
            if i == 0:
                z += 1
            if i != 0:
                y *= i
        if z > 1:
            return [0 for i in range(len(nums))]
        res = []

        for i in range(len(nums)):
            if nums[i] != 0:
                res.append(int(x/nums[i]))
            else:
                res.append(int(y))

        return res
                