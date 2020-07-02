#include <stdio.h>
#include <stdlib.h>


int isPrime(long int * array, long int num, int len);


int main()
{
    long int * primes = (long int *)malloc(10001 * sizeof(long int));
    int count = 0;
    long int num = 2;
    while (count < 10001)
    {
        if (isPrime(primes, num, count))
        {
            primes[count] = num;
            count++;
        }
        num++;
    }
    printf("%ld\n", primes[10000]);
    return 0;
}


int isPrime(long int * array, long int num, int len)
{
    for (int i = 0; i < len; i++)
    {
        if (num % array[i] == 0)
            return 0;
    }
    return 1;
}
