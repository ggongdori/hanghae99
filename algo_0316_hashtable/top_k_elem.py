class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_dict = {}
        ans = []
        for n in nums:
            if n not in num_dict:
                num_dict[n] = 1
            else:
                num_dict[n] += 1
        for k, v in num_dict.items():
            if v >= k:
                ans.append(k)
        return ans