#include <stdio.h>
#include <stdlib.h>


int fillFib(int * array, long int n);
long int findSum(int * array, int len);


int main()
{
    int * fib = (int *)calloc(1000, sizeof(int));
    long int n = 4000000;
    int len = fillFib(fib, n);
    n = findSum(fib, len);
    printf("%ld\n", n);
    return 0;
}


int fillFib(int * array, long int n)
{
    int i = 2;
    array[0] = 1;
    array[1] = 2;
    while (array[i-1] < n)
    {
        array[i] = array[i-1] + array[i-2];
        i++;
    }
    return i - 1;
}


long int findSum(int * array, int len)
{
    long int sum = 0;
    for (int i = 0; i < len; i++)
        if (array[i] % 2 == 0)
            sum += array[i];
    return sum;
}