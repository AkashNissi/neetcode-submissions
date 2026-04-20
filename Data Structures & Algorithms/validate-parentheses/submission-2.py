class Solution:
    def isValid(self, s: str) -> bool:
        m = {')':'(', ']':'[', '}':'{'}
        l = []

        for i in s:
            if l and i in m and l[-1] == m[i]:
                l.pop()
            else:
                l.append(i)

        return True if not l else False

    

        