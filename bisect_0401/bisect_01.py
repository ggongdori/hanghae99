import sys

input = sys.stdin.readline


def binary_search(target, array):
    array.sort()
    start = 0
    end = len(array) - 1

    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return mid
        elif array[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

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
        print("no")


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

    return binary_search_recursion(target, array, start, end)


# 테스트용 코드
if __name__ == '__main__':
    n = int(input())
    nums = list(map(int, input().split()))
    target = int(input())
    idx = binary_search_recursion(target, 0, 10, nums)

    if idx:
        print(nums[idx])
    else:
        print("no")
