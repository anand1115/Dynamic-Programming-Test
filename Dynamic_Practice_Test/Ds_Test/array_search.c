#include<stdio.h>

void main(){
    int a[10],i,n,search;
    printf("Enter the size of array : ");
    scanf("%d",&n);
    for(i=0;i<n;i++){
        scanf("\t%d",&a[i]);
    }
    printf("Enter Element to search : ");
    scanf("%d",&search);
    for(i=0;i<n;i++){
        if(a[i]==search){
            printf("%d",i);
            break;
        }
    }
}

