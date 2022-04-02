import sys

input = sys.stdin.readline

k, n = map(int, input().split())
lan_list = []
for _ in range(k):
    lan_list.append(int(input()))

print(lan_list)
# print(sum(lan_list) / n)

start, end = 1, max(lan_list)

while start <= end:
    mid = (start+end) // 2
    print(mid)
    #랜선 개수 카운트
    cnt = 0
    #현재 길이로 몇개나 만들 수 있는지 확인
    for lan in lan_list:
        cnt += lan // mid
        print(cnt)
    #원하는 개수 이상인 경우 더 길게 만들 수 있기 때문에
    #최대값은 유지하고 최소값을 1에서 mid+1
    if cnt >= n:
        start = mid + 1
        print(start)
    #원하는 개수를 만들지 못하면 더 잘라야 되기 때문에
    #최대값을 mid-1
    else:
        end = mid - 1
        print(end)

print(end)