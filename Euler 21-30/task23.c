#include <stdio.h>


int notAbSum(int num);
int isAb(int num);


int main()
{
    long int sum = 0;
    int n = 28123;
    for (int i = 1; i <= n; i++)
    {
        printf("%d\n", i);
        if (notAbSum(i))
            sum += i;
    }
    printf("%ld\n", sum);
    
    return 0;
}


int notAbSum(int num)
{
    for (int i = 1; i <= num / 2; i++)
        if (isAb(i) && isAb(num - i))
            return 0;
    return 1;
}


int isAb(int num)
{
    long int sum = 0;
    for (int i = 1; i < num; i++)
        if (num % i == 0)
            sum += i;
    if (num < sum)
        return 1;
    return 0;
}