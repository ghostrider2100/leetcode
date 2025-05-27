class Solution:
    def largestAltitude(self, gain: list[int]) -> int:

        #total = sum(gain)
        gt, total =  0, 0
        for n in gain:
            total += n
            if total > 0 and total > gt:
                gt = total

        #print (gt)
        return total

    def largestAltitude2(self, gain: list[int]) -> int:

        #total = sum(gain)
        gt, total =  0, 0
        mx = max(gain)
        mn = min(gain)
        print (mx, mn)
        #print (gt)
        return total


s = Solution()
# gain = [-5,1,5,0,-7]
gain = [-4,-3,-2,-1,4,3,2]
s.largestAltitude2(gain)