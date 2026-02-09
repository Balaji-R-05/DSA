def main():
  N, K = map(int, input().split())
  arr = list(map(int, input().split()))
  arr.sort()
  res = 0
  for i in range(N-K):
    res += arr[i]
  print(res)

if __name__ == "__main__":
  main()

# Time Complexity: O(N log N)
# Space Complexity: O(N)