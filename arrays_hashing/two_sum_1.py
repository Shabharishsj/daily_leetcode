# 1. Two Sum

######################################
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
# Runtime:n  6748 ms | Beats: 9.37%
# Memory: 15.2 MB | Beats: 26.5%


######################################
# using list

nums = [1, 2, 3, 4, 5]
target = 6
res = []

for i, n in enumerate(nums):
    diff = target - n
    if diff in res:
        print(i, res.index(diff))
        break
    res.append(n)
    
    
# TC: O(N) | SC: O(N^2)  
# Runtime: 1305 ms | Beats: 27.7%
# Memory: 14.9 MB | Beats: 96.15%


######################################
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
# Runtime: 122 ms | Beats: 69.94%
# Memory: 15 MB | Beats: 79.91%
            

# NOTES:
# Lookups in lists are O(n), lookups in dictionaries are O(1),
