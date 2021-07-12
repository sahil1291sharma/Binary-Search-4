class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        if n < m:
            return self.findMedianSortedArrays(nums2, nums1)
        low, high = 0, m
        while low <= high:
            partX = low + (high-low) //2
            partY = (m+n)//2 - partX
            L1 = float('-inf') if partX == 0 else nums1[partX - 1]
            L2 = float('-inf') if partY == 0 else nums2[partY - 1]
            R1 = float('inf') if partX == m else nums1[partX]
            R2 = float('inf') if partY == n else nums2[partY]
            if L1 <= R2 and L2 <= R1:
                if (m+n)%2 == 0:
                    return (max(L1, L2) + min(R1, R2))/2
                else:
                    return min(R1,R2)
            elif L1 > R2:
                high = partX-1
            else:
                low = partX+1
                
#Time complexity is O(logN) where N is the length of smaller array
#Space complexity is O(1) 