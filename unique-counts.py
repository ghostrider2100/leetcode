class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:

        arr.sort()
        uList = []
        ncntList = []

        for n in arr:
            if n not in uList:
                uList.append(n)

        #print (uList)

        for n in uList:
            ncnt = arr.count(n)
            if ncnt in ncntList:
                return False
            else:
                ncntList.append(ncnt)

        return True

so = Solution()

#arr = [1,2,2,1,1,3]
#arr= [1,2]
arr = [-3,0,1,-3,1,1,1,-3,10,0]

print (so.uniqueOccurrences (arr) )