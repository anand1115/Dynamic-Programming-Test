
def distinctIds(arr, n, mi):
    m = {}
    v = []
    count = 0

    for i in range(n):
        if arr[i] in m:
            m[arr[i]] += 1
        else:
            m[arr[i]] = 1

    for i in m:
        v.append([m[i],i])

    v.sort()
    size = len(v)

    for i in range(size):
        
        if (v[i][0] <= mi):
            mi -= v[i][0]
            count += 1
            
        else:
            return size - count
    return size - count

import heapq
def productIDheap(n, arr, m):
    maxheap = []
    for num in arr:
        heapq.heappush(maxheap, -num)

    for _ in range(m):
        heapq.heappop(maxheap)
    return len(set(maxheap))

def productIDsort(n, arr, m):
    arr.sort()
    return len(set(arr[:-m]))


arr = [1,1,1,2,3,2]
n = len(arr)

m = 2

print(distinctIds(arr, n, m))
print(productIDheap(n,arr,m))
print(productIDsort(n,arr,m))

