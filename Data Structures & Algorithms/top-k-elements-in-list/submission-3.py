class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        tup = set(nums)
        dick = {}
        for i in tup:
            dick[i] = (nums.count(i))
        if len(dick) == 1:
            return list(set(nums))
        a=sorted(dick.values())
        b=a[::-1]
        c = b[0:k]
        keys = [key for key, val in dick.items() if val in c]
        return keys