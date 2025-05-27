class Solution:
    def reverseVowels(self, s: str) -> str:

        s = list(s)
        vList = []
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        for l in s:
            if l in vowels:
                vList.append(l)

        #print (vList)

        vcnt = len(vList) - 1

        for n in range(0, len(s), 1):
            if s[n] in vowels:
                s[n] = vList[vcnt]
                vcnt -= 1

        return "".join(s)

    def reverseVowels2(self, s: str) -> str:

        s = list(s)
        vList = []
        #vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        vowels = ['a', 'e', 'i', 'o', 'u']
        for l in s:
            if l.lower() in vowels:
                vList.append(l)
        print(vList)

        vcnt = len(vList) - 1

        for n in range(0, len(s), 1):
            if s[n].lower() in vowels:
                s[n] = vList[vcnt]
                vcnt -= 1

        return "".join(s)

s = Solution()
word = "hello"
#print (s.reverseVowels(word) )

print (s.reverseVowels2(word) )

#for i in word:
#    print (i)
