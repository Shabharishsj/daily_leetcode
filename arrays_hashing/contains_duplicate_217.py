# 217. Contains Duplicate

# Brute Force
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    return True

        return False

# TC: O(N^2) | SC: O(1)


######################################
# my best try

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        res = list(set(nums))

        if len(nums) == len(res):
            return False
        else:
            return True

# TC: O(N) | SC: O(N)
# Runtime: 1075 ms | Beats: 45.37%
# Memory: 25.6 MB | Beats: 98.5%


######################################
# via sorting

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        nums.sort()

        for i in range(0, len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True

        return False

# TC: O(NlogN) | SC: O(1)
# Runtime:1234 ms | Beats: 16.39%
# Memory:26.2 MB | Beats:27.73%


######################################
# via hashmap

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        mydict = {}

        for i in nums:
            if i in mydict:
                return True
            else:
                mydict[i] = 1

        return False

# OR

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        myset = set()

        for i in nums:
            if i in myset:
                return True
            myset.add(i)

        return False


# TC: O(N) | SC: O(N)
# Runtime: 436 ms | Beats: 99.71%
# Memory: 26 MB | Beats: 67.49%

