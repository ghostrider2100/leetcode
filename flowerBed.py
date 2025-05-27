class Solution:

    '''You have a long flowerbed in which some of the plots are planted, and some are not.
    However, flowers cannot be planted in adjacent plots.
    Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty,
    and an integer n, return true if n new flowers can be planted in the flowerbed without violating
    the no-adjacent-flowers rule and false otherwise.'''

    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:

        print (flowerbed, n )

        if n <= 0:
            return True

        f = [0] + flowerbed + [0]

        for i in range(1, len(f) - 1, 1):
            if f[i - 1] == 0 and f[i] == 0 and f[i + 1] == 0:
                f[i] = 1
                n -= 1

            if n == 0:
                return True

        if n == 0:
            return True
        else:
            return False


s = Solution()

flowerbed = [1,0,0,0,1]; n = 1
print(s.canPlaceFlowers(flowerbed, n) )

flowerbed = [0,1,0,0,1]; n = 1
print (s.canPlaceFlowers(flowerbed, n) )

flowerbed = [1,0,0,0,1]; n = 2
print (s.canPlaceFlowers(flowerbed, n) )

flowerbed = [0]; n = 1
print (s.canPlaceFlowers(flowerbed, n) )

flowerbed = []; n = 1
print (s.canPlaceFlowers(flowerbed, n) )

flowerbed = [1,0,0,0,0,1]; n = 2
print (s.canPlaceFlowers(flowerbed, n) )

flowerbed = [1,0,1,0,1]; n = 0
print (s.canPlaceFlowers(flowerbed, n) )
