def missing_number(arr: list[int], n) -> int:
    total = n * (n + 1) // 2
    arr_sum = sum(arr)
    return total - arr_sum

arr = [1, 2, 3, 5, 6, 7, 8, 9]
n = 9
print(missing_number(arr, n))
