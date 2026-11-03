def main():
    side_1,side_2,side_3 = map(int,input().split())

    if (side_1 == side_2) or (side_2 == side_3) or (side_3 == side_1):
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()