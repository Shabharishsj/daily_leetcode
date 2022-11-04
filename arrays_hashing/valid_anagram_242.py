# 242. Valid Anagram

######################################
# brute force - NA


######################################
# using sort
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

# TC: O(NlogN) | SC: O(1) or O(N), based on the sorting algorith used.
# Runtime: 84 ms | Beats: 66.23%
# Memory: 15.1 MB | Beats: 21.76%


######################################
# using counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)

# TC: O(N) | SC: O(N)
# Runtime: 97 ms | Beats: 55.64%
# Memory: 14.4 MB | Beats 67.43%


######################################
# using hashmap
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        myset_s = {}
        myset_t = {}

        for i in range(len(s)):
            myset_s[s[i]] = 1 + myset_s.get(s[i], 0)
            myset_t[t[i]] = 1 + myset_t.get(t[i], 0)

        for j in myset_s:
            if myset_s[j] != myset_t.get(j, 0):
                return False

        return True

# TC: O(N) | SC: O(N)
# Runtime: 130 ms | Beats: 20.94
# Memory: 14.4 MB | Beats: 67.43%

# NOTES:
# can be solved with only one hashmap, increment key value by 1 when passing s and decrement by 1 when passing t
# If both are anagrams, the hashmap values should be 0 for all keys

