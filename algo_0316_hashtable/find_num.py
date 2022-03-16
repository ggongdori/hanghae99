import sys
from collections import defaultdict

input = sys.stdin.readline

N = int(input())
#값이 없을 시 에러가 날 수 있으니 int값을 갖는 defaultdict으로 초기화
nums_dict = defaultdict(int)

temp_list = list(map(int, input().split()))
M = int(input())
temp_list2 = list(map(int, input().split()))

for i in temp_list:
    if i not in nums_dict:
        nums_dict[i] = 1
    else:
        nums_dict[i] += 1

for j in temp_list2:
    if nums_dict[j] == 0:
        print(0)
    else:
        print(1)

