#include <stdio.h>


int divNum(long long int num);


int main()
{
    long long int num = 0, i = 1;
    while (i > 0)
    {
        num += i;
        if (divNum(num) > 500)
            break;
        i++;
    }
    printf("%lld\n", num);
    return 0;
}


int divNum(long long int num)
{
    int count = 0;
    for (long long int i = 1; i <= num / 2; i++)
        if (num % i == 0)
            count++;
    return count + 1;
}