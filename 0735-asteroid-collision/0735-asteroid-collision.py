# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for astrd in asteroids:
            while stack and astrd < 0 < stack[-1]:
                if stack[-1] < -1 * astrd:
                    # right-moving asteroid explodes, move onto next
                    stack.pop()
                    continue
                
                elif stack[-1] == -1 * astrd:
                    # both asteroids explode
                    stack.pop()
                    break

                # right-moving asteroid destroys left-moving, move to next asteroid in paramter
                break
            else:
                stack.append(astrd)

        return stack
            