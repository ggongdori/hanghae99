import heapq

def findKthLargest(self, nums, k):
    return sorted(nums, reverse=True)[k-1]



def findKthLargest(self, nums, k):
    heap = []
    for num in nums:
        heapq.heappush(heap, num)
    for _ in range(len(nums)-k):
        heapq.heappop(heap)
    return heapq.heappop(heap)






