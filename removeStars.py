class Solution:
    def removeStars(self, s: str) -> str:

        s = list(s)
        while "*" in s:
            idx = s.index('*')
            if idx > 0:
                s.pop(idx)
                s.pop(idx-1)

        return "".join(s)


    def removeStars2(self, s: str) -> str:

        s = list(s)
        stack = []

        for c in s:
            if c != '*':
                stack.append(c)
            else:
                stack.pop()
        return "".join(stack)




so = Solution()

ss = "leet**cod*e"
#ss = "erase*****"
print ( so.removeStars2(ss) )
