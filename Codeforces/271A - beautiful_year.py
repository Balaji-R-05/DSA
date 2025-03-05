# 271A - Beautiful Year

def is_special(yr: int) -> bool:
    return len(set(str(yr))) == 4  # Ensures all digits are unique

if __name__ == "__main__":
    yr = int(input())
    while True:
        yr += 1
        if is_special(yr):
            print(yr)
            break

# Time Complexity: O(1)
# Space Complexity: O(1)

