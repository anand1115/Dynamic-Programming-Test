#include<stdio.h>
union x{
    char i;
};
void main()
{

    char n=10;
    int *p=&n;
    printf("%d",x.i);

}
