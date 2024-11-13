# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        hash_map = {}

        res = 0

        for n in nums:
            if n in hash_map:
                # Pair found, decrement counter and add to result
                hash_map[n] -= 1
                res += 1

                # remove from hashmap so future occurances don't get messed up
                if hash_map[n] == 0:
                    del hash_map[n]

            else:
                # Number needed and the amount needed
                hash_map[k-n] = hash_map.get(k-n, 0) + 1

        return res
