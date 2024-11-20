# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        if not n:
            # can always place 0 flowers
            return True


        length = len(flowerbed)
        for i in range(length):

            # left is empty (true) if it doesnt exist or if it's is empty
            left = ((i==0) or (flowerbed[i-1]==0))

            # right is empty (true) if it doesnt exist or if it's is empty
            right = ((i==length-1) or (flowerbed[i+1]==0))


            if flowerbed[i] == 0 and left and right:
                flowerbed[i] = 1
                n -= 1

                if n <= 0:
                    return True      

        return False