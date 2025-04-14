def binary_search(arr: list[int], target:int) -> int:
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# if __name__ == "__main__":
#     arr = list(map(int, input().split()))
#     target = int(input())
#     print("Target not found in array" if binary_search(arr, target)==-1 else f"Target found at index {binary_search(arr, target)}")
