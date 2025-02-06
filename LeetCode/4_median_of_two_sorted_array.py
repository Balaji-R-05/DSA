# 4. Median of Two Sorted Arrays
from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l = []
        i=j=0
        l1 = len(nums1)
        l2 = len(nums2)
        while(i<l1 and j<l2):
            if nums1[i]<nums2[j]:
                l.append(nums1[i])
                i+=1
            else:
                l.append(nums2[j])
                j+=1
        while i<l1:
            l.append(nums1[i])
            i+=1
        while j<l2:
            l.append(nums2[j])
            j+=1
        if (l1+l2)%2==1:
            return l[(l1+l2)//2]
        else:
            m1 = l[(l1+l2)//2]
            m2 = l[(l1+l2)//2-1]
            return (m1+m2)/2
        
# Time complexity: O(n+m)
# Space complexity: O(n+m)

s = Solution()

# Test cases

print(s.findMedianSortedArrays(nums1=[1,3], nums2=[2]))
print(s.findMedianSortedArrays(nums1=[1,2], nums2=[3,4]))