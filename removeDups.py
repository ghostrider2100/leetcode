class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        cnt = 0
        c = 0
        while cnt < len(nums):
            cc = nums[c]
            if nums.count(cc) > 1:
                for n in range(0, nums.count(cc)-1, 1) :
                    nums.remove(cc)
            cnt += 1
            c +=1

            print (nums)
            return(len(nums))

    def removeDuplicates2(self, nums: list[int]) -> int:
        unique_list = list(dict.fromkeys(nums))
        print (unique_list)
        return(len(unique_list))

    def removeDuplicates3(self, nums: list[int]) -> int:

        newList = []
        for i in nums:
            if i not in newList:
                newList.append(i)
        print (newList)
        return len(newList)






c = Solution()
#c.removeDuplicates([1,1,2])
#c.removeDuplicates2([0,0,1,1,1,2,2,3,3,4])

#c.removeDuplicates2([1,1,2])
#c.removeDuplicates2([0,0,1,1,1,2,2,3,3,4])

c.removeDuplicates3([1,1,2])
#c.removeDuplicates2([0,0,1,1,1,2,2,3,3,4])

