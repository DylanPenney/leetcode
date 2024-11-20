# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        current_minimum = float('inf')
        current_penutimate_minimum = float('inf')

        for num in nums:
            if num <= current_minimum:
                # if the current number is the new minmum, 
                # update it
                current_minimum = num
            elif num <= current_penutimate_minimum:
                # likewise but for second minimum(hence the ELIF)
                current_penutimate_minimum = num
            else:
                # found a triplet
                return True

        return False
