#include<stdio.h>
void main(){
    int a[10],size,val,pos,n,i;
    size=sizeof(a)/sizeof(a[0]);
    printf("Enter number of elements to add : ");
    scanf("%d",&n);
    if(n>size){
        printf("Array size is exceeded !!");
    }
    else{
        printf("Enter array elements : ");
        for(i=0;i<n;i++){
            scanf("\t%d",&a[i]);
        }
        printf("Array element to insert : \n");
        if(n==size-1){
            printf("Can't insert element : ");
        }
        else{
            printf("insert at : ");
            scanf("%d",&pos);
            if(pos>size-1){
                printf("Please add valid position : ");
            }
            else{
                for(i=n-1;i>=pos;i--){
                    a[i+1]=a[i];
                }
                printf("Enter value to insert : ");
                scanf("%d",&val);
                a[pos]=val;
                n+=1;
                for(i=0;i<n;i++){
                    printf("%d ",a[i]);
                }
            }
        }

    }

}

