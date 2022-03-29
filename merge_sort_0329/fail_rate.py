import sys


def solution1(N, stages):
    cnt = 0
    fail_rate = []

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
    return fail_rate



def solution2(N, stages):
    stages.sort()
    answer = []
    length = len(stages)
    fail = []
    k = 0
    for i in range(1, N + 1):
        count = 0
        for j in range(k, len(stages)):
            k = j
            if stages[j] == i:
                count += 1
            else:
                break
        if length == 0:
            f = 0
        else:
            f = count / length
        fail.append((i, f))
        length = length - count

    # fail.sort(reverse=True, key=lambda x:x[1])
    fail.sort(key=lambda x: (-x[1]))
    for f in fail:
        answer.append(f[0])
    return answer

input = sys.stdin.readline

N = int(input())
stages = [2,1,2,6,2,4,3,3]


print(solution1(N, stages))
print(solution2(N, stages))