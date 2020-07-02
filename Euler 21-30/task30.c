#include <stdio.h>
#include <math.h>


long int sumNums(long int n);


int main()
{
    long int sum = 0;
    for (long int i = 2; i <= 295246; i++)
        if (sumNums(i) == i)
            sum += i;
    printf("%ld\n", sum);
    return 0;
}


long int sumNums(long int n)
{
    long int sum = 0;
    while (n > 0)
    {
        sum += pow(n % 10, 5);
        n /= 10;
    }
    return sum;
}