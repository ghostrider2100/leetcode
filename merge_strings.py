class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        newlist = []
        w1cnt, w2cnt = 0, 0

        while w1cnt < len(word1) and w2cnt < len(word2):
            newlist.append(word1[w1cnt])
            newlist.append(word2[w2cnt])
            w1cnt += 1
            w2cnt += 1

        if len(word1) != len(word2):
            if len(word1) > len(word2):
                newlist.append(word1[w1cnt:])

            elif len(word2) > len(word1):
                newlist.append(word2[w2cnt:])

        return "".join(newlist)

s = Solution()

word1 = "abc"; word2 = "pqr"
#word1 = "ab"; word2 = "pqrs"
#word1 = "cdf"; word2 = "a"


print (s.mergeAlternately(word1, word2) )




