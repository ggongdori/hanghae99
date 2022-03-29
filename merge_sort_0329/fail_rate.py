import sys

input = sys.stdin.readline

N = int(input())

cnt = 0
fail_rate = []
stages = [2,1,2,6,2,4,3,3]
leng = len(stages)
# stages.sort(reverse=True) #[6,4,3,3,2,2,2,1]

for i in range(1, N+1):
    cnt = stages.count(i)
    if leng == 0:
        fail = 0
    else:
        fail = cnt / leng

    fail_rate.append((i, fail))
    leng -= cnt

fail_rate = sorted(fail_rate, key = lambda x:x[1], reverse=True)

fail_rate = [i[0] for i in fail_rate]
print(fail_rate)



