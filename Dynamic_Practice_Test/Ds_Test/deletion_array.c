#include<stdio.h>
void main(){
    int a[10]={1,3,4},n=3,i,d=1;
    for(i=d+1;i<n;i++){
        a[i-1]=a[i];
    }
    for(i=0;i<n-1;i++){
        printf("%d ",a[i]);
    }

}
