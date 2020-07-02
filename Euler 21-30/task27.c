#include <stdio.h>
#include <math.h>


int isPrime(int num);
int maxNum(int a, int b);


int main()
{
    long int a, b;
    int len = 0;
    int temp;
    for (int i = -999; i < 1000; i++)
        for (int j = -1000; j <= 1000; j++)
        {
            temp = maxNum(i, j);
            if (temp > len)
            {
                len = temp;
                a = i;
                b = j;
            }
        }
    printf("%ld", a * b);
    return 0;
}


int isPrime(int num)
{
    if (num <= 1)
        return 0;
    for (int i = 2; i < num; i++)
        if (num % i == 0)
            return 0;
    return 1;
}


int maxNum(int a, int b)
{
    int x = 2, n = -1;
    while (isPrime(x))
    {
        n++;
        x = pow(n, 2) + a * n + b;
    }
    return n;
}