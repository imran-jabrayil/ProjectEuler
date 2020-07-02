#include <stdio.h>


int checkSum(long int num);
long int fact(int num);


int main()
{
    long int sum = 0;
    printf("%ld\n\n", fact(9));
    for (long int i = 10; i < 9999999; i++)
        if (checkSum(i))
            sum += i;
    printf("%ld\n", sum);
    return 0;
}


int checkSum(long int num)
{
    long int sum = 0;
    while (num > 0)
    {
        sum += fact(num % 10);
        num /= 10;
    }
    if (num == sum)
        return 1;
    return 0;
}


long int fact(int num)
{
    if (num == 1)
        return 1;
    return num * fact(num - 1);
}