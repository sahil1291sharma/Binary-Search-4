class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums1)
        m = len(nums2)
        
        if n > m: return self.intersect(nums2, nums1)
        
        hashMap = {}
        result = []
        for x in nums2:
            if x in hashMap:
                hashMap[x] +=1
            else:
                hashMap[x] = 1
        
        for y in nums1:
            if y in hashMap:
                result.append(y)
                hashMap[y] -=1
                if hashMap[y] == 0:
                    hashMap.pop(y)
            print(hashMap)
        
        return result
            
#Time complexity O(M) + O(N) 
#Space complexity O(M)
        