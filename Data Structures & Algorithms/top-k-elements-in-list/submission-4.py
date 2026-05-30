class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        x = {}
        for i, val in enumerate(nums):
            x[val] = 1 + x.get(val, 0)
        #{1: 1, 2: 2, 3: 3}
        y = sorted(x.items(), key = lambda item: item[1], reverse = True)

        z = []

        for i in range(k):
            z.append(y[i][0])
        
        return z
        
