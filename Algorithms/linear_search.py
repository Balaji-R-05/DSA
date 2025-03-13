def linear_search(arr: list[int], target: int) -> int:
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    target = int(input())
    print("Target not found in array" if linear_search(arr, target)==-1 else f"Target found at index {linear_search(arr, target)}")