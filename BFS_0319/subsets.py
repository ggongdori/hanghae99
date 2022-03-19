
def subsets(self, nums):


    self.res = []
    self.dfs(nums, 0, [])
    return self.res

def dfs(self, nums, pos, tmp):
    self.res.append(tmp)
    for i in range(pos, len(nums)):
        self.dfs(nums, i + 1, tmp + [nums[i]])
