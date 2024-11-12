# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        if guess(1) == 0:
            return 1

        lo = 1
        hi = n
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            res = guess(mid)
            if res == 0:
                return mid
            
            if res == -1:
                # mid is higher
                hi = mid -1
            else:
                lo = mid + 1
            
        