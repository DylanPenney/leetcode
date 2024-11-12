# Time Complexity: O(logN)
# Space Complexity: O(1)
class Solution:
    def guessNumber(self, n: int) -> int:
        l = 0
        r = n
        while l <= r:
            mid = l + (r-l)//2

            res = guess(mid)
            if res == 0:
                # We have found the correct number:
                return mid
            
            elif res == 1:
                # Our guess is too low, move l pointer
                l = mid + 1
                
            else:
                # Our guess is to high, move r pointer
                r = mid - 1