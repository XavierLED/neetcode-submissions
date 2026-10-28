class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.target = k
        self.n = nums
        heapq.heapify(self.n)

        while len(self.n) > k:
            heapq.heappop(self.n)

    def add(self, val: int) -> int:
        heapq.heappush(self.n, val)

        while len(self.n) > self.target:
            heapq.heappop(self.n)

        return self.n[0]
        
