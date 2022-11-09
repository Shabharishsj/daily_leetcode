
# 238. Product of Array Except Self

##############################################
# using prefix and suffix with extra space

A = [1, 2, 3, 4, 5]

# ans: [120,60,40,30,24]

n = len(A)

#prefix
prefix = [1] * n
prefix[0] = A[0]

for i in range(1,n):
    prefix[i] = prefix[i-1] * A[i]
print(prefix)

#suffix
suffix = [1] * n
suffix[n-1] = A[n-1]

for i in range(n-2,-1,-1):
    suffix[i] = suffix[i+1] * A[i]
print(suffix)

#product 
res = [1] * n 
res[0] = suffix[1]
res[n-1] = prefix[n-2]

for i in range(1,n-1):
    res[i] = prefix[i-1] * suffix[i+1]
    
print(res)


# TC: O(N) | SC: O(N)
# Runtime: 258 ms | Beats: 86.18%
# Memory: 22.4 MB | Beats: 18.47%

##################################################
# using prefix and suffix without extra space

A = [1, 2, 3, 4, 5]

n = len(A)
res = [1] * n

prefix = 1
for i in range(n):
    res[i] = prefix
    prefix *= A[i] 

suffix = 1
for i in range(n-1,-1,-1):
    res[i] *= suffix
    suffix *= A[i] 

print(res)

# TC: O(N) | SC: O(1)
# Runtime: 555 ms | Beats: 48.19%
# Memory: 21.4 MB | Beats: 58.91%
