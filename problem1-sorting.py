class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        n = len(nums1)
        m = n-1
        if n%2 == 0:
            return (nums1[m//2] + nums1[m//2 + 1])/2
        else:
            return nums1[m//2]
        
#Brute force solution with time complexity O(M+NlogM+N) M -> len(nums1) N -> len(nums2)
#Space complexity O(M+N)