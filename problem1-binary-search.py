class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums1)
        m = len(nums2)
        
        if n > m: return self.intersect(nums2, nums1)
        
        nums1.sort()
        nums2.sort()
        result = []
        low, high = 0, m-1
        
        for i in range(n):
            curr = nums1[i]
            bsIdx = self.binarySearch(nums2, low, high, curr)
            if bsIdx is not -1:
                low = bsIdx + 1
                result.append(curr)
        
        return result
    
    def binarySearch(self, nums, low, high, target):
        while low <= high:
            mid = low + (high - low) //2
            if nums[mid] == target: 
                if mid == low or nums[mid-1] < nums[mid]:
                    return mid
                else:
                    high = mid -1
            elif nums[mid] > target:
                high = mid -1
            else:
                low = mid + 1
        return -1
                    
            

#Time complexity O(NlogM) where M is number of elements in the larger array and N is number of elements in smaller array
#Space complexity is O(1)        