class Solution:
    def majorityElement(self, nums: list[int]) -> int:

        uniqList = []
        for n in nums:
            if n not in uniqList:
                uniqList.append(n)
        tcnt = 0
        nn = None
        for i in uniqList:
            if nums.count(i) > tcnt:
                tcnt = nums.count(i)
                nn = i
        return nn

    def majorityElement2(self, nums: list[int]) -> int:

        uniqDict = {}
        for n in nums:
            if n not in uniqDict.keys():
                uniqDict[n] = 1
            else:
                uniqDict[n] = uniqDict[n] +1

        mv = max(uniqDict.values())
        print ("mv", mv)
        ll = list(uniqDict.keys())[list(uniqDict.values()).index(mv)]
        #print ("ll", ll )
        return ll

sol = Solution()
#print (sol.majorityElement([2,2,1,1,1,2,2]))
print (sol.majorityElement2([2,2,1,1,1,2,2]))
