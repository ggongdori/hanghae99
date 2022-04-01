import sys

input = sys.stdin.readline

def binary_search(target, array):
    array.sort()
    start = 0
    end = len(array) - 1

    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return mid # 함수를 끝내버린다.
        elif array[mid] < target:
            start = mid + 1
        else:
            end = mid -1

    return None

# 테스트용 코드
if __name__ == "__main__":

    n = int(input())
    nums = list(map(int, input().split()))
    target = int(input())
    idx = binary_search(target, nums)

    if idx:
      print(nums[idx])
    else:
      print("찾으시는 타겟 {}가 없습니다".format(target))

# recursive

def binary_search_recursion(target, array, start, end):
    if start > end:
        return None

    mid = (start + end) // 2

    if array[mid] == target:
        return mid
    elif array[mid] > target:
        end = mid - 1
    else:
        start = mid + 1

    return binary_search_recursion(target, start, end, array)

# 테스트용 코드
if __name__ == '__main__':
    n = int(input())
    nums = list(map(int, input().split()))
    target = int(input())
    idx = binary_search_recursion(target, 0, 10, nums)

    print(nums)
    print(idx)