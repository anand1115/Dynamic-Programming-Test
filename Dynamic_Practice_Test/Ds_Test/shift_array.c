#include<stdio.h>

void method1(int arr[],int n,int r){
    int i,temp,j;
    for(j=0;j<r;j++){
        temp=arr[0];
        for(i=0;i<n-1;i++){
            arr[i]=arr[i+1];
        }
        arr[n-1]=temp;
    }

}
void method2(int arr[],int n,int r){
    int i,j,temp[r];
    r=r%n;
    for(i=0;i<r;i++){
        temp[i]=arr[i];
    }
    for(i=0;i<n-r;i++){
        arr[i]=arr[i+r];
    }
    int k=0;
    for(i=n-r;i<n;i++){
        arr[i]=temp[k];
        k++;
    }
}
void method2_right(int arr[],int n,int r){
    int i,j,temp[r],k;
    r=r%n;
    for(i=n-r;i<n;i++){
        temp[i]=arr[i];
    }
    for(i=n-1;i<n;i++){
        arr[i]=arr[i-r];
    }
    for()

}


void method1_left(int arr[],int n,int r){
    int i,j,temp;
    for(j=0;j<r;j++){
        temp=arr[n-1];
        for(i=n-1;i>0;i--){
            arr[i]=arr[i-1];
        }
        arr[0]=temp;
    }
}

void main(){
    int a[100],n,i,r;
    printf("Please Enter Size of array : ");
    scanf("%d",&n);
    printf("Please Enter Elements : ");
    for(i=0;i<n;i++){
        scanf("\t%d",&a[i]);
    }
    printf("Please Enter shifting size : ");
    scanf("%d",&r);
    method2(a,n,r);
    for(i=0;i<n;i++){
        printf("%d ",a[i]);
    }
}
