import heapq as heap

#힙 없이
def findKthLargest(self, nums, k):
    return sorted(nums, reverse=True)[k-1]



def findKthLargest(self, nums, k):
    h = []
    # heap.heapify(nums)
    #숫자들을 힙에 넣어줌
    #최소 힙이기에 가장 작은 수가 루트 노드
    for num in nums:
        heap.heappush(h, num)
    #k번째 큰 수 =
    for _ in range(len(nums)-k):
        heap.heappop(h)
    return heap.heappop(h)

def findKthLargest(self, nums: List[int], k: int) -> int:
    h = heap.heapify(nums)
    length = len(nums)
    while length > k:
        h.heappop(nums)
        length -= 1
    return nums[0]





