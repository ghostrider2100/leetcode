class Solution:

    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        #code goes here
        if len(ransomNote) > len(magazine):
            return False
        ransomNote = list(ransomNote)
        magazine = list(magazine)
        #print (ransomNote, magazine)

        for c in ransomNote:
            if c in magazine:
                idx = magazine.index(c)
                magazine.pop(idx)
                continue
            else:
                return False

        return True





    def canConstruct2(self, ransomNote: str, magazine: str) -> bool:
        #code goes here
        if len(ransomNote) > len(magazine):
            return False
        ransomNote = "".join(sorted(ransomNote))
        magazine = "".join(sorted(magazine))
        print (ransomNote, magazine)

        if ransomNote in magazine:
            return True
        else:
            return False
        #for c in magazine:

s = Solution()
#ransomNote = "aa"; magazine = "aab"
#ransomNote ="aab";  magazine ="baa"

ransomNote ="bg";  magazine = "efjbdfbdgfjhhaiigfhbaejahgfbbgbjagbddfgdiaigdadhcfcj"



print (s.canConstruct(ransomNote, magazine) )
