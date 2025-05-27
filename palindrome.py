import re

class Solution:
    import re
    def isPalindrome(self, s: str) -> bool:

        s = s.lower()
        print (s)
        result = re.sub('[\W_]+', '', s)
        print (result)

        ls = list(result)
        ln = len(ls)
        cnt = 0
        for l in ls:
            if l != ls[ln-cnt-1]:
                return False
            cnt += 1

        return True



        #ss = "".join(reversed(s) )
        #print (ss)



s = Solution()
#ss = "A man, a plan, a canal: Panama"
#ss = "race a car"
ss = ""

print ( s.isPalindrome(ss) )