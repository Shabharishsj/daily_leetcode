
# 49. Group Anagrams 


######################################
# using hashmap 

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res = defaultdict(list)
        
        for i in strs:
            count = [0] * 26
            
            for c in i:
                count[ord(c)-ord("a")] += 1

            res[tuple(count)].append(i)
        
        return res.values()
      
# TC: O(N*M) M -> length of each strings | SC: O(N) 
# Runtime: 170 ms | Beats: 74.30%
# Memory: 19.9 MB | Beats: 9.88%

