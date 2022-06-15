class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        eleset = set(s)
        if len(s) == len(t):
            for i in eleset:
                if s.count(i) != t.count(i):
                    return False
            return True


# https://leetcode.com/problems/valid-anagram/
