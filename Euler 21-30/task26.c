#include <stdio.h>
#include <stdlib.h>


int findCycle(int num);
int inArray(int * array, int num, int len);


int main()
{
    int num, temp;
    int len = 0;
    for (int i = 1; i < 1000; i++)
    {
        temp = findCycle(i);
        if (temp > len)
        {
            len = temp;
            num = i;
        }
    }
    printf("%d", num);
    return 0;
}


int findCycle(int num)
{
    int * remains = (int *)calloc(num, sizeof(int));
    int temp = 1, count = 0;
    while (temp != 0)
    {
        temp %= num;
        remains[count] = temp;
        if (inArray(remains, temp, count) > -1)
        {
            free(remains);
            return count - inArray(remains, temp, count);
        }
        count++;
        temp *= 10;
    }
    return 0;
}


int inArray(int * array, int num, int len)
{
    for (int i = 0; i < len; i++)
        if (array[i] == num)
            return i;
    return -1;
}