# 1. Two Sum

# Brute Force

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for i in range(0,len(nums)):
            
            for j in range(i,len(nums)):
            
                if j == i:
                    continue
            
                if nums[i] + nums[j] == target:
                    return [i,j]
                
# TC: O(N^2) | SC: O(1)   
# Runtime: 122 ms | Beats: 69.94%
# Memory: 15.2 MB | Beats: 26.5%


# using Hashmap 

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        mydict = {}

        for i,n in enumerate(nums):
            diff = target - n
            if diff in mydict:
                return [i,mydict[diff]]
            mydict[n] = i
            
            
# TC: O(N) | SC: O(N)     
# Runtime: 6748 ms | Beats: 9.37%
# Memory: 15 MB | Beats: 79.91%
            
