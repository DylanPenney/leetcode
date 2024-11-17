# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for char in s:

            if char != "]":
                stack.append(char)

            else:
                curr = ""
                while stack[-1] != "[":
                    curr = stack.pop() + curr

                stack.pop() # remove the '['

                repeated_times = ""

                while stack and stack[-1].isdigit():
                    repeated_times = stack.pop() + repeated_times

                stack.append(int(repeated_times) * curr)

        return "".join(stack)

