class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapp={
            ')':'(',
            ']':'[',
            '}':'{'
        }
        for i in s:
            if i in mapp.values():
                stack.append(i)
            elif i in mapp.keys():
                if not stack or mapp[i]!= stack.pop():
                    return False
        return not stack
    

a = Solution()
print(a.isValid("([)]"))