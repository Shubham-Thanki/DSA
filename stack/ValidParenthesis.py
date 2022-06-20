class Solution:
    def isValid(self, s: str) -> bool:
        openStack = []
        Dict = {'(': ')', '{': '}', '[': ']'}

        for i in range(len(s)):
            if s[i] not in Dict:
                # If stack is empty initially, and ')'}']' comes, it will return false directly
                if openStack and s[i] == Dict[openStack[-1]]:
                    openStack.pop()
                else:
                    return False
            else:
                openStack.append(s[i])
        if not openStack:
            return True
        else:
            return False

# https://leetcode.com/problems/valid-parentheses/
