from typing import List
from collections import defaultdict
import bisect


def lis_of_k(arr: List[int], k):
    n = len(arr)
    dic = defaultdict(list)

    for i,val in enumerate(arr):
        imod = i%k
        idx = bisect.bisect_right(dic[imod], val)
        if idx == len(dic[imod]):
            dic[imod].append(val)
        else:
            dic[imod][idx] = val

    acc = 0
    for key,lst in dic.items():
        ln = (n-1-key)//k + 1
        acc += ln-len(lst)

    return acc


if __name__ == '__main__':
    print(lis_of_k([2,4,1,3], 1))  # 2
    print(lis_of_k([2,4,1,3], 2))  # 2
    print(lis_of_k([2,4,1,3,2,4,1,3,2,4,1,4,4,4], 3))  # 4
    print(lis_of_k([1, 17, 5, 10, 13, 15, 10, 5, 16, 18], 1))  # 3
    print(lis_of_k([3, 5, 6, 2, 5, 4, 19, 5, 6, 7, 12], 1))  # 4
    print(lis_of_k([5, 5, 6, 5, 5, 5, 5], 1))  # 1
