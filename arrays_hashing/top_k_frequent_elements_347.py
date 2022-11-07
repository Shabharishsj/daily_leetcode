# 347. Top K Frequent Elements

######################################
# using hashmap and list

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {}
        freq = [[] for i in range(len(nums)+1)]

        for n in nums:
            count[n] = 1 + count.get(n,0)

        for n,c in count.items():
            freq[c].append(n)

        res = []

        for i in range(len(freq)-1,0,-1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

# TC: O(N) | SC: O(N)
# Runtime: 271 ms | Beats: 22.16%
# Memory: 19.7 MB | Beats: 6.1%

