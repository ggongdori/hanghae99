import sys
from collections import defaultdict
input = sys.stdin.readline

#저장된 사이트 수, 비번 찾으려는 사이트 수
N, M= map(int, input().split())
pw_dict = defaultdict(str)
temp_list=[]
input_list = []
ans = []
# print(pw_dict)

# print(input().split())

# print(key)
# print(val)

for _ in range(N):
    temp_list.append(list(map(str, input().split())))
for _ in range(M):
    input_list.append(str(input().rstrip()))

# print(input_list)
for t in temp_list:
    pw_dict[t[0]] = t[1]

for s in input_list:
    if s in pw_dict.keys() is not None:
        print(pw_dict[s])


# print(temp_list)
# for i in range(N):
#     pw_dict[key_list[i]] = val_list[]
# print(key_list)
# print(val_list)
# print(pw_dict)


