# Time Complexity: O(logn)
# Space Complexity: O(1)
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        
        # can't be first or last index
        l = 1
        r = len(arr) - 2

        while l <= r:
            m = l + (r-l)//2

            if arr[m-1] < arr[m]:
                
                
                if arr[m] > arr[m+1]:
                    # peak index
                    return m

                l = m + 1

            else:
                r = m - 1

        