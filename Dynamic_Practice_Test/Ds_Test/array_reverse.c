#include<stdio.h>
void main(){
    int n,i,j,start,end,temp;
    printf("Enter the values of n :");
    scanf("%d",&n);
    int arr[n];
    for(i=0;i<n;i++){
        scanf("\t%d",&arr[i]);
    }
    start=0;
    end=n-1;
    while(start<end){
        temp=arr[start];
        arr[start]=arr[end];
        arr[end]=temp;
        start+=1;
        end-=1;
    }
    for(i=0;i<n;i++){
        printf("%d ",arr[i]);
    }
}
