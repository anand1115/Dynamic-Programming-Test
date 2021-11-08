def lcs(s1,s2,s3,x,y,z):
    if(x==0 or y==0 or z==0):
        return 0
    else:
        if(s1[x-1]==s2[y-1] and s2[y-1]==s3[z-1]):
            return 1+lcs(s1,s2,s3,x-1,y-1,z-1)
        else:
            return max(lcs(s1,s2,s3,x,y,z-1),lcs(s1,s2,s3,x,y-1,z),lcs(s1,s2,s3,x-1,y,z))


def lcs_dynamic(s1,s2,s3,x,y,z,memo={}):
    key=str(x)+":"+str(y)+":"+str(z)
    if key in memo:
        return memo[key]
    if(x==0 or y==0 or z==0):
        return 0
    else:
        if(s1[x-1]==s2[y-1] and s2[y-1]==s3[z-1]):
            memo[key]=1+lcs_dynamic(s1,s2,s3,x-1,y-1,z-1,memo)
            return memo[key]
        else:
            memo[key]=max(lcs_dynamic(s1,s2,s3,x,y,z-1),lcs_dynamic(s1,s2,s3,x,y-1,z),lcs_dynamic(s1,s2,s3,x-1,y,z))
            return memo[key]
    
s1=input()
s2=input()
s3=input()
print(lcs_dynamic(s1,s2,s3,len(s1),len(s2),len(s3)))
