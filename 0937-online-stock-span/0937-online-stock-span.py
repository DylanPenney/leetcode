# Time Complexity: O(n)
# Space Complexity: O(n)
class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        stack = self.stack
        res = 1
        while stack and price >= stack[-1][0]:
            _, stack_span = stack.pop()
            res += stack_span
        stack.append((price, res))
        return res

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)