class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:

        nums = sorted(nums)
        while val in nums:
            n = nums.index(val)
            nums.pop(n)
        #print (nums)
        #return len(nums)
        return (nums)


s = Solution()
#print (s.removeElement([3,2,2,3], 3)   )

print (s.removeElement([0,1,2,2,3,0,4,2], 2))