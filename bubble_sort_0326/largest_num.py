def largestNumber2(self, nums):
    for i in range(len(nums), 0, -1):
        for j in range(i - 1):
            if not self.compare(nums[j], nums[j + 1]):
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return str(int("".join(map(str, nums))))


def compare(self, n1, n2):
    return str(n1) + str(n2) > str(n2) + str(n1)




def largestNumber4(self, nums):
    for i in range(len(nums)):
        pos, cur = i, nums[i]
        while pos > 0 and not self.compare(nums[pos-1], cur):
            nums[pos] = nums[pos-1]  # move one-step forward
            pos -= 1
        nums[pos] = cur
    return str(int("".join(map(str, nums))))