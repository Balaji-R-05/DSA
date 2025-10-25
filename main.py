def main():
    def solve(lst, target):
        hmap = {}
        count = 0
        for num in lst:
            complement = target - num
            if complement in hmap:
                count += 1
            hmap[num] = hmap.get(num, 0) + 1
        return count
    lst = [1, 2, 3, 4, 3, 2, 1]
    target = 4
    print(solve(lst, target))

if __name__ == "__main__":
    main()