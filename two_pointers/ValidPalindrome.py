class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        s = s.casefold()
        while l < r:
            while l < r and not self.alphaNum(s[l]):
                l += 1
            # We use while loop here to increment the pointer incase
            # we encounter consecutive non-alphanumeric characters in the string.
            while l < r and not self.alphaNum(s[r]):
                r -= 1
            if s[l] != s[r]:
                return False
            l, r = l+1, r-1
        return True

    def alphaNum(self, c):
        return (ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))


# https://leetcode.com/problems/valid-palindrome/
