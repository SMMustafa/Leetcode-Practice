from collections import Counter
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:

        count = Counter(words)
        heap = [(-v,k) for k,v in count.items()]
        heapq.heapify(heap)

        return [heapq.heappop(heap)[1] for _ in range(k)]
