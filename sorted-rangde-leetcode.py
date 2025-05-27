class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        newList = []
        for a in range(0, m, 1):
            newList.append(nums1[a])
            #print (newList)

        for b in range(0, n, 1):
            newList.append(nums2[b])
            #print (newList)

        #print(sorted(newList))
        nums1=newList.copy()
        nums1 = sorted(nums1)
        #return (sorted (newList))

    def merge2(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:

        for a in range(len(nums1), len(nums1)-m, -1):
            nums1.pop(a-1)
            print (nums1)

        for b in range(0, n, 1):
            nums1.append(nums2[b])
            print (sorted(nums1) )

c = Solution()
#print ( c.merge([1,2,3,0,0,0],3, [2,5,6], 3) )

print ( c.merge2([1,2,3,0,0,0],3, [2,5,6], 3) )