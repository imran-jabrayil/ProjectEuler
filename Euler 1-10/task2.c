#include <stdio.h>
#include <stdlib.h>


long int calculate(long int limit);


int main()
{
    long int limit = 4000000;
    printf("%ld\n", calculate(limit));
    return 0;
}



long int calculate(long int limit)
{
    long int temp, sum = 0;
    long int fib1 = 1, fib2 = 1;
    while (fib1 <= 4000000)
    {
        if (fib1 % 2 == 0)
            sum += fib1;
        temp = fib1 + fib2;
        fib1 = fib2;
        fib2 = temp;
    }
    return sum;
}