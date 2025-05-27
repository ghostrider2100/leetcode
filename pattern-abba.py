class Solution:
    # https://leetcode.com/problems/word-pattern/submissions/1270849337/?envType=study-plan-v2&envId=top-interview-150

    # https://leetcode.com/problems/design-hashset/
    def wordPattern(self, pattern: str, s: str) -> bool:
        ds = {}
        ns = []
        ps = list (p)
        ss = s.split()

        #print (ps); print (ss)

        if (len(ps) != len(ss)) or len(ps) == 0:
            return False

        cnt = 97
        for item in ss:
            if item not in ds.values():
                ds[cnt] = item
                cnt += 1

        #print (ds)

        for pp in ps:
            print ( ord(pp) )
            ns.append(ds[ord(pp)])

        print (ns)
        nc = 0
        for item in ns:
            if item != ss[nc]:
                return False
            nc += 1
        return True


sc = Solution()
p = "abba"
#p = "aaaa"

s = "dog dog dog dog"

#s = "dog cat cat dog"
#s = "dog cat cat dog"
#s =  "dog cat cat fish"
print (sc.wordPattern(p, s) )


