class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        try:
            return (haystack.index(needle) )
        except:
            return -1


s = Solution()

#h = "sadbutsad"
#n= "sad"

h = "leetcode"
n = "leeto"


print (s.strStr(h, n))