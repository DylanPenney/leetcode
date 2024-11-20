# Time Complexity: O(logn)
# Spaec Complexity: O(n)
class RecentCounter:

    def __init__(self):
        self.queue = []

    def ping(self, t: int) -> int:
        self.queue.append(t)

        cutoff = t - 3000
        l = 0
        r = len(self.queue) - 1

        while (l < r):
            m = l + (r-l)//2

            if self.queue[m] < cutoff:
                l = m + 1
            else:
                r = m
        
        self.queue = self.queue[r:]

        return len(self.queue)

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)