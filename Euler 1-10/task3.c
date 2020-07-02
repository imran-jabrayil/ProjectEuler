#include <stdio.h>
#include <stdlib.h>
#include <math.h>


int isPrime(long int * array, long int num, long int len);
long int findPrime(long int * array, long long int num, long int len);

int main()
{
    long long int n = 600851475143;
    long int count = 0;
    long int * primes = (long int *)malloc(floor(sqrt(n)) * sizeof(long int));
    for (long int i = 2; i < floor(sqrt(n)); i++)
        if (isPrime(primes, i, count))
        {
            primes[count] = i;
            count++;
        }
    printf("%ld\n", findPrime(primes, n, count));
    return 0;
}


int isPrime(long int * array, long int num, long int len)
{
    for (long int i = 0; i < len; i++)
        if (num % array[i] == 0)
            return 0;
    return 1;
}


long int findPrime(long int * array, long long int num, long int len)
{
    for (long int i = len - 1; i >= 0; i--)
        if (num % array[i] == 0)
            return array[i];
    return 0;
}