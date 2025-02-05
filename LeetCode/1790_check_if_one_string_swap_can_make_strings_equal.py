# 1790. Check if One String Swap Can Make Strings Equal

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        count = 0
        j = -1
        k = -1
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                count+=1
                if j==-1: j = i
                elif k==-1: k=i
        if count ==0 : return True
        elif count==2 and s1[k]==s2[j] and s1[j]==s2[k]: return True
        return False
    
# Time complexity: O(n)
# Space complexity: O(1)

# Approach: Check if the strings are equal or not. If they are equal return True. If they are not equal
# then check if there are only 2 characters which are different and if the characters at the different
# indexes are same in both the strings. If yes, return True else return False.

# Optimized approach: Instead of using 2 variables to store the indexes of the different characters, we can
# use a single variable to store the index of the first different character and then store the index of the
# second different character in the same variable if the first different character is already stored. This
# will reduce the space complexity of the code.

print(Solution().areAlmostEqual("bank", "kanb")) # True
print(Solution().areAlmostEqual("attack", "defend")) # False
print(Solution().areAlmostEqual("kelb", "kelb")) # True



