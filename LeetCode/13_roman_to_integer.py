# 13. Roman to Integer

class Solution:
    def romanToInt(self, s: str) -> int:
        d = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        count = i = 0
        while(i<len(s)):
            if s[i]=="I" and i!=len(s)-1:
                if s[i+1]=="V":
                    count+=4
                    i+=2
                elif s[i+1]=="X":
                    count+=9
                    i+=2
                else:
                    count+=d[s[i]]
                    i+=1
            elif s[i] == "X" and i!=len(s)-1:
                if s[i+1]=="L":
                    count+=40
                    i+=2
                elif s[i+1]=="C":
                    count+=90
                    i+=2
                else:
                    count+=d[s[i]]
                    i+=1
            elif s[i] == "C" and i!=len(s)-1:
                if s[i+1]=="D":
                    count+=400
                    i+=2
                elif s[i+1]=="M":
                    count+=900
                    i+=2
                else:
                    count+=d[s[i]]
                    i+=1
            else:
                count+=d[s[i]]
                i+=1
        return count
    
# Time complexity: O(n)
# Space complexity: O(1)

# Testcase
solution = Solution()

print(solution.romanToInt("III")) # 3
print(solution.romanToInt("IV")) # 4
print(solution.romanToInt("IX")) # 9
print(solution.romanToInt("LVIII")) # 58
print(solution.romanToInt("MCMXCIV")) # 1994
print(solution.romanToInt("X")) # 10

