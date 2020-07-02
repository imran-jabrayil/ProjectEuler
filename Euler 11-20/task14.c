#include <stdio.h>


int findLen(long int num, int len);


int main()
{
    int len = 0, temp;
    long int ans;
    for (long int i = 1; i < 1000000; i++)
    {
        temp = findLen(i, len);
        if (temp > len)
        {
            len = temp;
            ans = i;
        }
    }
    printf("%ld\n", ans);
}


int findLen(long int num, int len)
{
    int count = 1;
    while (num != 1)
    {
        if (num % 2 == 0)
            num /= 2;
        else 
            num = num * 3 + 1;
        count++;
    }
    return count;
}