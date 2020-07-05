#include <stdio.h>
#include <time.h>


int notAbSum(int num);
int isAb(int num);


int main()
{
    time_t start, end;
    start = time(NULL);
    long int sum = 0;
    int n = 28123;
    for (int i = 1; i <= n; i++)
        if (notAbSum(i))
            sum += i;
    printf("%ld\n", sum);
    end = time(NULL);
    printf("Time %lf s.", difftime(end, start));
    return 0;
}


int notAbSum(int num)
{
    for (int i = 1; i <= num / 2; i++)
        if (isAb(i) && isAb(num - i))
            return 0;
    return 1;
}


int isAb(int num)
{
    long int sum = 0;
    for (int i = 1; i <= num / 2; i++)
    {
        if (num % i == 0)
            sum += i;
        if (num < sum)
            return 1;
    }
    return 0;
}