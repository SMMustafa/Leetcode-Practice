from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = Counter(nums)

        heap = [(-v, k) for k,v in count.items()]
        heapq.heapify(heap)
        return [heapq.heappop(heap)[1] for i in range (k)]
