#include <stdio.h>
#include <math.h>


long int sumOfSq(int n);
long int sqOfSum(int n);


int main()
{
    printf("%ld", sqOfSum(100) - sumOfSq(100));
    return 0;
}


long int sumOfSq(int n)
{
    long int sum = 0;
    for (int i = 1; i <= n; i++)
        sum += i*i;
    return sum;
}


long int sqOfSum(int n)
{
    long int sum = 0;
    for (int i = 1; i <= n; i++)
        sum += i;
    return sum * sum;
}