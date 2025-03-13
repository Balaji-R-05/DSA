def kadane(arr: list[int]) -> int:
    max_sum = float("-inf")
    current_sum = 0
    for i in arr:
        current_sum += i
        if current_sum > max_sum:
            max_sum = current_sum
        if current_sum < 0:
            current_sum = 0
    return max_sum

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    print(kadane(arr))