class Solution:
    def isValid(self, s: str) -> bool:
        'build a stack to hold and pop'
        stack = []
        'use hashmap to have a open and close bracekts map'
        hashmap ={')':'(', ']': '[', '}': '{'}
        'loop through s'
        for i in s:
            if i in hashmap:
                if stack and stack[-1] == hashmap[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        'return true if stack is empty else false'   
        return True if not stack else False  