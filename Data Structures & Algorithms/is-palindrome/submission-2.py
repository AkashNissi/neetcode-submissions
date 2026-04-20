class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = [i.lower() for i in s if i.isalnum()]
        b = a[::-1]
        return a == b

        