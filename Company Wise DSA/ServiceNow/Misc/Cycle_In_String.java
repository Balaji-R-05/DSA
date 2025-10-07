// You have an array of strings, and we can connect two strings, if last letter of one string is same as the first letter of other string. For example ABC CDE can be connected to make ABC-CDE. Now, you have to find out, if a cycle can be made by joining the strings in this fashion .
// Example Input : array=[“ABC”, “CDE”, “EFA”]
// Output : Yes
// Example Input : array=[“ABC”, “CDE”, “EFG”]
// Output : No



// I told him that, we can simply make a graph, by connecting every possible pair of strings, and then we just need to use any standard algorithm for cycle detection. He then asked me to write the code for cycle detection in graph. He appreciated for the quick response, and was satisfied with my code. I was then asked the following DP problem

// Input Handling:
// I first read the number of strings and stored them in an array.

// Graph Construction:
// I treated each character as a node and created a directed edge from the first character to the last character of each string.
// I used a HashMap<Character, List<Character>> to represent the adjacency list.
// graph.computeIfAbsent(start, k -> new ArrayList<>()).add(end);


// Cycle Detection (DFS):
// I wrote a standard DFS-based cycle detection algorithm for a directed graph:

// Maintain two sets: visited and inStack.
// If a node being explored is already in the recursion stack → a cycle exists.

// Result:
// If a cycle was detected, I printed "Yes", otherwise "No".


import java.util.*;

public class Cycle_In_String {
    static Map<Character, List<Character>> graph = new HashMap<>();
    static Set<Character> visited = new HashSet<>();
    static Set<Character> inStack = new HashSet<>();
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        sc.nextLine();
        String[] arr = new String[n];
        for (int i = 0; i < n; i++) arr[i] = sc.nextLine();
        
        for (String s: arr) {
            char start = s.charAt(0);
            char end = s.charAt(s.length() - 1);
            graph.computeIfAbsent(start, k -> new ArrayList<>()).add(end);
        }

        boolean hasCycle = false;
        for(char node: graph.keySet()) {
            if(!visited.contains(node)) {
                if(dfs(node)) {
                    hasCycle = true;
                    break;
                } 
            }
        }
        System.out.println(hasCycle ? "Yes" : "No");
        sc.close();
    }

    static boolean dfs(char node) {
        visited.add(node);
        inStack.add(node);
        for(char neighbor: graph.getOrDefault(node, new ArrayList<>())) {
            if (!visited.contains(neighbor)) {
                if (dfs(neighbor)) return true;
            } else if (inStack.contains(neighbor)) {
                return true;
            }
        }
        inStack.remove(node);
        return false;
    }
}
