import collections
def count_(s, k):
    s = list(s)
    def atMost(k):
        count = collections.defaultdict(int)
        left = 0
        ans = 0
        for right, x in enumerate(s):
            count[x] += 1
            while len(count) > k:
                count[s[left]] -= 1
                if count[s[left]] == 0:
                    del count[s[left]]
                left += 1
            ans += right - left + 1
        return ans
    return atMost(k) - atMost(k-1)
def countkDist(str1, k):
    n = len(str1)
    res = 0
    cnt = [0] * 27
    for i in range(0, n):
        dist_count = 0
        cnt = [0] * 27
        for j in range(i, n):
            if(cnt[ord(str1[j]) - 97] == 0):
                dist_count += 1
            cnt[ord(str1[j]) - 97] += 1
            if(dist_count == k):
                res += 1
            if(dist_count > k):
                break
    return res  
str1 = "pqpqs"
k = 2
print("Total substrings with exactly", k,"distinct characters : ", end = "")
print(countkDist(str1, k))
print(count_(str1, k))

