def main():
  n = int(input())
  arr = list(map(int, input().split()))
  if arr[0] > arr[1]:
    print(arr[0])
    return
  if arr[-1] > arr[-2]:
    print(arr[-1])
    return
  
  l = 1
  r = n-2
  while (l < r):
    mid = (l+r) // 2
    if (arr[mid-1] < arr[mid]) and (arr[mid] > arr[mid+1]):
      print(arr[mid])
    if (arr[mid] < arr[mid + 1]):
      l = mid + 1;
    else:
      r = mid - 1;
    
  print(arr[r])

if __name__ == "__main__":
  main()