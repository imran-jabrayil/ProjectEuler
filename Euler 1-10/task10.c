#include <stdio.h>
#include <stdlib.h>


int isPrime(long int * array, long int num, long int len);
long int findSum(long int * array, long int len);


int main()
{
    long int count = 0;
    long int * primes = (long int *)malloc(2000000*sizeof(long int));
    for (long int i = 2; i < 2000000; i++)    
    {
        if (isPrime(primes, i, count))
        {
            primes[count] = i;
            count++;
        }
    }
    printf("%ld\n", findSum(primes, count));
    return 0;
}


int isPrime(long int * array, long int num, long int len)
{
    for (int i = 0; i < len; i++)
        if (num % array[i] == 0)
            return 0;
    return 1;
}


long int findSum(long int * array, long int len)
{
    long int sum = 0;
    for (long int i = 0; i < len; i++)
        sum += array[i];
    return sum;
}