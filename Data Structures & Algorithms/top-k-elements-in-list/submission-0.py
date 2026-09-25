class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = defaultdict(list)

        for num in nums:
            hashmap[num] = 1 + hashmap.get(num, 0)
        
        heap = []

        for num in hashmap:
            heapq.heappush(heap, (hashmap[num], num))
            if len(heap) > k:
                heapq.heappop(heap)
        res = []

        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res