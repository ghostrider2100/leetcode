class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:

        nnews1 = []
        for i in nums1:
            if i not in nnews1:
                nnews1.append(i)

        nnews2 = []
        for j in nums2:
            if j not in nnews2:
                nnews2.append(j)

        nnews3 = [[]]
        for k in nnews1:
            if k not in nnews2:
                nnews3[0].append(k)
            else:
                idx = nnews2.index(k)
                del nnews2[idx]
                
        nnews3.append(nnews2)
        return(nnews3)


    def findDifference1(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:

        nnews1 = []
        for i in nums1:
            if i not in nnews1:
                nnews1.append(i)

        nnews2 = []
        for j in nums2:
            if j not in nnews2:
                nnews2.append(j)

        nnews3 = [[]]
        for k in nnews1:
            if k not in nnews2:
                nnews3[0].append(k)
            else:
                idx = nnews2.index(k)
                del nnews2[idx]

        nnews3.append(nnews2)
        return(nnews3)








s = Solution()

nums1 = [1,2,3]; nums2 = [3,4,5]

print (s.findDifference(nums1, nums2) )

