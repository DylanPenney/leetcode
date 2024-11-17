class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # binary search on [1...max(piles)]
        # if we find a value (eating rate) that is possible to eat with, then search below it
        # return minimum value that works
        
        l = 1 # can't be 0/hour
        r = max(piles)
        
        res = r # must be less than or equal to the max in the list

        while l <= r:
            mid = l + (r - l) // 2 # <--- this is k

            hours_to_eat_all = 0
            for pile in piles:
                hours_to_eat_all += math.ceil(pile/mid)

            if hours_to_eat_all <= h:
                # new res, garunteed to be lower than previous one
                res = mid

                # search lower
                r = mid - 1
            
            else:
                # search higher, as this rate is not enought to eat all bananas
                l = mid + 1

        return res