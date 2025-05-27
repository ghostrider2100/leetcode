class Solution:
    def reverseWords(self, s: str) -> str:
        #s = s.strip()
        s= s.split()
        s= s[::-1]
        #s="".join(s)." "
        ns = []
        for w in s:
            ns.append( w + " ")

        #ns = ("".join(ns)).strip()
        return ("".join(ns)).strip()


s = Solution()
st = "        hello world      "

print(s.reverseWords(st))