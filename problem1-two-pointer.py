class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums1)
        m = len(nums2)
        
        if n > m: return self.intersect(nums2, nums1)
        
        nums1.sort()
        nums2.sort()
        result = []
        p1, p2 = 0, 0
        
        while p1 < n and p2 < m:
            if nums1[p1] == nums2[p2]:
                result.append(nums1[p1])
                p1 += 1
                p2 += 1
            elif nums1[p1] > nums2[p2]:
                p2 += 1
            else:
                p1 += 1
        
        return result

#Time complexity O(M) where M is number of elements in the larger array ignoring the sorting time
#Space complexity is O(1)        