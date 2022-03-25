def findKthLargest1(self, nums, k):
    return sorted(nums, reverse=True)[k-1]