from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dick = defaultdict(list)

        for i in range(len(strs)):
            dick[tuple(sorted(strs[i]))].append(strs[i])

        return list(dick.values())

        