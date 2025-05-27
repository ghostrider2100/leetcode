
class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        nns = []
        for i in nums:
            nns.append (abs(i))

        nnums = sorted(nns)
        print ( nnums )

        nls = nnums[len(nnums)-k:len(nnums)]
        print (nls)




s = Solution()
nums = [1,12,-5,-6,50,3]; k = 4
s.findMaxAverage(nums, k)



