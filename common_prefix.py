class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:

        word = strs[0]
        for item in strs:
            if len(item) < len(word):
                word = item
        print (word)

        wc = list(word)
        mm = ""
        print (wc)
        for c in wc:
            for sw in strs:
                if c not in sw:
                    break
                else:
                    mm = mm + c
        return mm



s = Solution()

strings = ["flower","flow","flight"]

print (s.longestCommonPrefix(strings) )

