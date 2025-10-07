from collections import defaultdict

def dfs(node, graph, visited, rec_stack):
    visited.add(node)
    rec_stack.add(node)

    for neighbor in graph[node]:
        if neighbor not in visited:
            if dfs(neighbor, graph, visited, rec_stack):
                return True
        elif neighbor in rec_stack:
            return True

    rec_stack.remove(node)
    return False


def can_form_cycle(strings):
    graph = defaultdict(list)
    for s in strings:
        start = s[0]
        end = s[-1]
        graph[start].append(end)

    visited = set()
    rec_stack = set()

    for node in graph:
        if node not in visited:
            if dfs(node, graph, visited, rec_stack):
                return True
    return False


# 3️⃣ Input + Output
if __name__ == "__main__":
    n = int(input("Enter number of strings: "))
    strings = [input().strip() for _ in range(n)]

    if can_form_cycle(strings):
        print("Yes")
    else:
        print("No")
