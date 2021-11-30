#include<stdio.h>
void main(){
    int n,i,j;
    printf("Enter the size of the array : ");
    int arr[n];
    for(i=0;i<n;i++){
        scanf("\t%d",&arr[i]);
    }
    for(i=0;i<n;i++){
        printf("%d\t",arr[i]);
    }
}
