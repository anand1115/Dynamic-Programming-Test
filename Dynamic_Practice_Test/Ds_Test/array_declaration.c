#include<stdio.h>
void main(){
    int a[10];
    printf("%d %d\n",a[2],a[-3]);//prints random integer because not intilized
    //printf("%d",a[1.2]); raises error because index must be integer only
    //int a[]={1,3,3};#raises error because of redeclaration
    int arr[3]={1,3,4};
    printf("%d %d \n",sizeof(arr),sizeof(arr[0]));
    int ar[10]={1,3}; //rest elemets initise with zeros
    printf("%d %d %d \n",ar[9],ar[1],sizeof(ar));
    int array[]={};//empty array with zero size and elements
    printf("%d\n",sizeof(array));
    int* arr1={1,3,4};
    printf("%d \n",*arr1);
}
