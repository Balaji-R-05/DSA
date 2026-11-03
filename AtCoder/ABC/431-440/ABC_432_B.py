def main():
    s = input().strip()
    digits = sorted(s)
    if digits[0] == '0':
        for i, d in enumerate(digits):
            if d != '0':
                first = digits.pop(i)
                result = first + "".join(digits)
                print(result)
                return
    print("".join(digits))

if __name__ == "__main__":
    main()