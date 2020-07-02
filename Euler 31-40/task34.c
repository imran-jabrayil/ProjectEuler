#include <stdio.h>


int checkSum(long int num);
long int fact(int num);


int main()
{
    long int sum = 0;
    for (long int i = 10; i < 2540160; i++)
        if (checkSum(i))
            sum += i;
    printf("%ld\n", sum);
    return 0;
}


int checkSum(long int num)
{
    long int sum = 0;
    long int temp = num;
    while (temp > 0)
    {
        sum += fact(temp % 10);
        temp /= 10;
    }
    if (num == sum)
        return 1;
    return 0;
}


long int fact(int num)
{
    if (num == 0)
        return 1;
    return num * fact(num - 1);
}