import heapq

#힙 없이
def findKthLargest(self, nums, k):
    return sorted(nums, reverse=True)[k-1]



def findKthLargest(self, nums, k):
    heap = []
    #숫자들을 힙에 넣어줌
    #최소 힙이기에 가장 작은 수가 루트 노드
    for num in nums:
        heapq.heappush(heap, num)
    #k번째 큰 수 =
    for _ in range(len(nums)-k):
        heapq.heappop(heap)
    return heapq.heappop(heap)

def findKthLargest(self, nums: List[int], k: int) -> int:
    heap = heapq.heapify(nums)
    length = len(nums)
    while length > k:
        heap.heappop(nums)
        length -= 1
    return nums[0]





