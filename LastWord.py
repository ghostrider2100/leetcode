

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        ss = s.strip()
        ml = ss.split(' ')
        print (ml)
        mll = len(ml)
        word = ml[mll-1]
        return len(word)

    def lengthOfLastWord2(self, s: str) -> int:
        ml = (s.strip()).split(' ')
        word = ml[len(ml)-1]
        return len(word)

s = Solution()
#ss = "Hello World"
ss = "   fly me   to   the moon  "
print ( s.lengthOfLastWord2(ss) )

in