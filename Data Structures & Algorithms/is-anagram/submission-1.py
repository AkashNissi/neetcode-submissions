class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        c_s, c_t = {}, {}

        for i in range(len(s)):
            c_s[s[i]] = c_s.get(s[i], 0) + 1
            c_t[t[i]] = c_t.get(t[i], 0) + 1
        for i in c_s:
            if c_s[i] != c_t.get(i, 0):
                return False
        return True
        