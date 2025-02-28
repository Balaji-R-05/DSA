# 1678. Goal Parser Interpretation

class Solution:
    def interpret(self, command: str) -> str:
        new_command = []
        n = len(command)
        for i in range (n):
            if (command[i]=='G'):
                new_command.append('G')
            elif (command[i] == '('):
                if (command[i+1] == ')'):
                    new_command.append('o')
                    i+=1
                elif (command[i+1] == 'a'):
                    new_command.append('al')
                    i+=3
        return ("".join(map(str, new_command)))
    
# Time complexity: O(n)
# Space complexity: O(n)



class Solution:
    def interpret(self, command: str) -> str:
        return command.replace("()","o").replace("(al)","al")
    
# Time complexity: O(n)
# Space complexity: O(n)

