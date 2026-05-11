import heapq

# 只需要维护最大的k个数
# 用一个小顶堆维护最大的k个数

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = nums
        self.k = k
        heapq.heapify(self.heap)

        while len(self.heap)>self.k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        while len(self.heap)>self.k:
            heapq.heappop(self.heap)
        return self.heap[0]
        
