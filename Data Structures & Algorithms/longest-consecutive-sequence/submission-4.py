class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        x = list(set(nums))
        x.sort()
        # print(x)
        longest = 1
        current = 1
        for i in range(len(x) - 1):
            if x[i+1] == x[i] + 1:
                current += 1
            else:
                current = 1
            longest = max(longest, current)
        if not nums:
            return 0
        return longest
        