def main():
    nums = list(map(int, input().split()))
    nums = sorted(nums)                 
    nums = list(map(str, nums))         
    print("".join(nums[::-1]))                  

if __name__ == "__main__":
    main()