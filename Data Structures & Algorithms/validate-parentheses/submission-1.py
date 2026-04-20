class Solution:
    def isValid(self, s: str) -> bool:
        stac = []
        h = { ')':'(', ']':'[', '}':'{' }
        
        for i in s:
            if i in h: 
                if stac and stac[-1] == h[i]:
                    stac.pop()
                else:
                    return False
            else:
                stac.append(i)

        return True if not stac else False

        