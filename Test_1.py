def myfun(a,b,c):
    final=float('inf')
    x,y=a+1,b-1
    i,j=a-1,b+1
    final=min(abs(a+c-(2*b)),final)
    final=min(abs(i+c-(2*j)),final)
    y,x=a+1,b-1
    j,i=a-1,b+1
    final=min(abs(a+c-(2*b)),final)
    final=min(abs(i+c-(2*j)),final)
    return final
input_list=list(map(int,input().split()))
ans=myfun(*input_list)
ans=min(ans,myfun(input_list[1],input_list[2],input_list[0]))
ans=min(ans,myfun(input_list[2],input_list[0],input_list[1]))
print(ans)



    
