class Solution:
    def isValid(self, s: str) -> bool:
        mp = {')':'(',']':'[', '}':'{' }


        stack = []
        for char in s:
            if char in mp.values():
                stack.append(char)
            else:
                if not stack or stack[-1] != mp[char]:
                    return False
                else:
                    stack.pop()
        if len(stack) == 0:            
            return True
        return False
