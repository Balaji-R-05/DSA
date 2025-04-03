# 1598. Crawler Log Folder

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stk = ["mn"]
        for operation in logs:
            if operation == "./":
                continue
            elif operation == "../" and len(stk) > 1:
                stk.pop()
            else:
                if operation[0] != ".":
                    stk.append(operation)
            
        return len(stk)-1
    
# Time Complexity: O(n), where n is the number of logs.
# Space Complexity: O(n), where n is the number of logs.