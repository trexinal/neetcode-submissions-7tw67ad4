class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        forward = "({["
        backward = ")}]"

        for i in range(len(s)):
            if s[i] in forward:
                stack.append(s[i])
            if s[i] in backward:
                pair = backward.index(s[i])
                if stack:
                    if forward[pair] == stack[-1] and s[i] == backward[pair]:
                        print(s[i] + backward[pair])
                        stack.pop()
                    else:
                        return False
                else: 
                    return False
        return stack == []