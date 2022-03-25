import sys

input = sys.stdin.readline
flag = True
T = int(input())

for _ in range(T):
    flag = True
    n = int(input())
    phone_num = [input().rstrip() for _ in range(n)]
    phone_num.sort()
    num = phone_num[0]

    for i in range(len(phone_num)-1):
        length = len(phone_num[i])
        if phone_num[i+1][:length] == phone_num[i]:
            flag = False

    if flag == True:
        print("yes")
    else:
        print("no")

