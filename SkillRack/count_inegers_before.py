# Count Integers Before

"""

Count Integers Before
Given an Integer array nums of length N, for each nums[i], the program must print how many numbers in the array are smaller than it. That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].
Boundary Condition(s):
1 <= N <= 10^5
0 <= Each integer value <= 10^9
Input Format:
The first line contains N.
The second line contains N integer values.
Output Format:
The first line contains N integer values.
Example Input/Output 1:
Input:
4
40 10 20 30
Output: 3012
Example Input/Output 2:
Input:
3
65 65 65
Output:
000
"""



import heapq
def count_before(arr):
    l_arr = [(num,idx) for idx,num in enumerate(arr)]
    heapq.heapify(l_arr)
    
    count = -1
    prev = None
    while l_arr:
        num,idx = heapq.heappop(l_arr)
        if num==prev:
            arr[idx] = count
        else:
            count+=1
            arr[idx] = count
            prev = num
    
    return arr
    
arr = [65, 65, 65]
res = count_before(arr)
print(res)