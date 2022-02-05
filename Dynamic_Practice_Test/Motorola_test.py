
class Solution:
	def check(self,low, upp):
		for i in range(26):
			if (low[i] != 0 and (upp[i] == 0)):
				return 0

			elif((low[i] == 0) and (upp[i] != 0)):
				return 0
		return 1
	def solution(self,s):
		low,upp = [0 for i in range(26)],[0 for i in range(26)]
		for i in range(len(s)):
			if (ord(s[i]) >= 65 and ord(s[i]) <= 90):
				upp[ord(s[i]) - 65] += 1
			else:
				low[ord(s[i]) - 97] += 1
		mp = {}
		for i in range(26):
			if (low[i] and upp[i]==0):
				mp[chr(i + 97)] = 1

			elif (upp[i] and low[i]==0):
				mp[chr(i + 65)] = 1
		for i in range(len(low)):
			low[i] = 0
			upp[i] = 0
		i = 0
		st = 0
		start = -1
		end = -1
		minm = float('inf')

		while (i < len(s)):
			if(s[i] in mp):
			
				while (st < i):
					if (ord(s[st]) >= 65 and ord(s[st]) <= 90):
						upp[ord(s[st]) - 65] -= 1
					else:
						low[ord(s[st]) - 97] -= 1

					st += 1
				i += 1
				st = i
			else:
				if (ord(s[i]) >= 65 and ord(s[i]) <= 90):
					upp[ord(s[i]) - 65] += 1
				else:
					low[ord(s[i] )- 97] += 1
				while (1):
					if (ord(s[st]) >= 65 and ord(s[st])<= 90 and upp[ord(s[st])- 65] > 1):
						upp[ord(s[st]) - 65] -= 1
						st += 1
					elif (ord(s[st]) >= 97 and ord(s[st]) <= 122 and low[ord(s[st]) - 97] > 1):
						low[ord(s[st]) - 97] -= 1
						st += 1
					else:
						break

				if (self.check(low, upp)):
					if (minm > (i - st + 1)):
						minm = i - st + 1
						start = st
						end = i
				i += 1
		if (start == -1 or end == -1):
			return -1
		else:
			final = ""
			for i in range(start,end+1,1):
				final += s[i]
			return len(final)


print(Solution().solution(input()))


