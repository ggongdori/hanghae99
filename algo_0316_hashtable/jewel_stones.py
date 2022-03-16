class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewel_dict = {}
        cnt = 0
        for s in stones:
            if s not in jewel_dict:
                jewel_dict[s] = 1
            else:
                jewel_dict[s] += 1

        for j in jewels:
            if j in stones:
                cnt += jewel_dict[j]
        return cnt