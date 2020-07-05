#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <time.h>


int isAb(int num);
int fillAb(int * array, int limit);
bool isSum(int num, int * array, int limit);
bool inArray(int num, int * array, int limit, int index);


int main()
{
    time_t start = time(NULL);
    int n = 28123;
    int * abus = (int *)calloc(n, sizeof(int));
    int limit = fillAb(abus, n);
    long int sum = 0;
    for (int i = 1; i <= n; i++)
        if (!isSum(i, abus, limit))
            sum += i;
    printf("%ld\n", sum);
    printf("Time: %lf s.\n", difftime(time(NULL), start));
    return 0;
}


int isAb(int num)
{
    long int sum = 0;
    for (int i = 1; i <= num / 2; i++)
        if (num % i == 0)
            sum += i;
    if (num < sum)
        return 1;
    return 0;
}


int fillAb(int * array, int limit)
{
    int index = 0;
    for (int i = 1; i <= limit; i++)
        if (isAb(i))
        {
            array[index] = i;
            index++;
        }
    return index;
}


bool isSum(int num, int * array, int limit)
{
    for (int i = 0; i < limit; i++)
    {
        if (array[i] > num / 2)
            return false;
        if (inArray(num - array[i], array, limit, i))
            return true;
    }
    return false;
}


bool inArray(int num, int * array, int limit, int index)
{
    for (int i = index; i < limit; i++)
        if (num == array[i])
            return true;
    return false;
}