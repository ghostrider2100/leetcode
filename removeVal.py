class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        print(nums.count(val))
        #cnt = 0
        while val in nums:
            idx = nums.index(val)
            nums.pop(idx)
            #cnt +=1
        print (nums, len(nums))
        #print (cnt)
        return (len(nums) )

c = Solution()
#c.removeElement([3,2,2,3],3)

c.removeElement([0,1,2,2,3,0,4,2],2)
