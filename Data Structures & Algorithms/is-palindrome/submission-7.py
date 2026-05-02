class Solution:
    def isPalindrome(self, s) -> bool:
        a = ''.join(filter(str.isalnum, s)).lower()
        return a == a[::-1]