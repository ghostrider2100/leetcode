class Solution:

    def gcdOfStrings1(self, str1: str, str2: str) -> str:

        if len(str1) < 1 or len(str2) < 1:
            return ""

        test = True
        while test:

            for ic2 in range(len(str2),0, -2) :
                if str2.count(str2[:ic2]) * len(str2[:ic2]) != len(str2):
                    continue
                if str1.count(str2[:ic2]) * len(str2[:ic2]) == len(str1):
                    return str2[:ic2]
            test = False

        t2 = str2.count(str2[:1])
        if t2 * len(str2[:1]) != len(str2):
            return ""
        t1 = str1.count(str2[:1])
        if t1 * len(str2[:1]) == len(str1):
            return str2[:1]



    def gcdOfStrings2(self, str1: str, str2: str) -> str:

        if len(str1) < 1 or len(str2) < 1:
            return ""

        test = True
        while test:

            for ic2 in range(len(str2),0, -1) :
                t2 = str2.count(str2[:ic2])
                if t2 * len(str2[:ic2]) != len(str2):
                    continue
                t1 = str1.count(str2[:ic2])
                if t1 * len(str2[:ic2]) == len(str1):
                    return str2[:ic2]
            return ""
            test = False

s = Solution()

#str1 = "ABCABC"; str2 = "ABC"
#str1 = "ABABAB"; str2 = "ABAB"
#str1 = "AAAAA"; str2 = "AA"
#str1 = "TAUXXTAUXXTAUXXTAUXXTAUXX"; str2 = "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX"
str1 = ""; str2 = "AA"

print ( s.gcdOfStrings1(str1, str2) )

#ABABABABAB == ABABABABAB

#n = [1, 2, 3]
#print (sum(n))

#print ( s.gcdOfStrings(str1, str2) )