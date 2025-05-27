class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        if len(nums) > 3:
            nt = nums.copy()
            nt.sort()
            idx = len(nt) -1
            while nt[idx] //2 >= target:
                idx = idx // 2
                #print (idx)

            #print (nt)
            #print (idx)

        print (nums[:idx])

        for n in range(0, len(nums), 1):

            np = n+1
            for nn in range(np, len(nums), 1):

                if nums[n] + nums[nn] == target:
                    print ([n, nn])
                    return ([n, nn])


        return []

so = Solution()


#nums = [3,2,4]

target = 0
nums = [0,4,3,0]

#nums = [3,2,4, 10, 11, 15, 22, 30, 45]

#target = 6
#target = 11

so.twoSum(nums, target)