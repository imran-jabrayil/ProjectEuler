#include <stdio.h>


long int friendly(long int num);

int main()
{
    long int sum = 0;
    for (int i = 1; i < 10000; i++)
        if (i == friendly(friendly(i)) && i != friendly(i))
            sum += i;
    printf("%ld\n", sum);
    return 0;
}


long int friendly(long int num)
{
    long int sum = 0;
    for (int i = 1; i < num; i++)
        if (num % i == 0)
            sum += i;
    return sum;
}