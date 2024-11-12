# Time Complexity: O(nlogn)
# Space Complexity: O(n)
class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        beans.sort()
        n = len(beans)
        total_beans = sum(beans)
        res = float('inf')

        for index, num_of_beans in enumerate(beans):
            res = min(res, total_beans - ((n - index) * num_of_beans))
        
        return res

