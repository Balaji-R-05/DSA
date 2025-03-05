# 158A - Next Round

def next_round():
    n, k = map(int, input().split())
    scores = list(map(int, input().split()))

    threshold = scores[k - 1]
    count = sum(1 for score in scores if score >= threshold and score > 0)

    print(count)
    
if __name__ == "__main__":
    next_round()

# Time Complexity: O(n)
# Space Complexity: O(n)