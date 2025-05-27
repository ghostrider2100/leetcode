class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:

  if len(nums) == 0:
            return []
        res_nums = []
        bstart = True
        lc = 0
        while lc < len(nums):
            if bstart == True:
                start = nums[lc]
                end = start
                cnt = 1
                bstart = False
                #print (start, end)
                lc += 1
                continue
            if (start + cnt) == nums[lc]:
                cnt += 1
                end = nums[lc]
                lc += 1
                continue
            else:
                if start == end:
                    res = str(start)
                else:
                    res = str(start) + "->" + str(end)
                res_nums.append(res)
                bstart = True

        if start == nums[lc-1] or  end == nums[lc-1]:
            if start == end:
                res_nums.append(str(start) )
            else:
                res = str(start) + "->" + str(end)
                res_nums.append(res)

        return res_nums

s = Solution()
#nums = [0,1,2,4,5,7]
#nums = [0,1,2]
#nums = [0]
nums = [0,2,3,4,6,8,9]
print (s.summaryRanges(nums))

# Output: ["0->2","4->5","7"]

# https://leetcode.com/problems/summary-ranges/description/?envType=study-plan-v2&envId=top-interview-150





