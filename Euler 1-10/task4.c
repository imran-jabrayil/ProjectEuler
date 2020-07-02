#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int isPalindrome(long int n);
int numLen(long int n);


int main()
{
    long int temp, ans = 0;
    for (int i = 999; i >= 100; i--)
        for (int j = 999; j >= 100; j--)
        {
            temp = i * j;
            if (isPalindrome(temp) && temp > ans)
            {
                ans = temp;
            }
        }
    printf("%ld", ans);
    return 0;
}


int isPalindrome(long int n)
{
    int len = numLen(n);
    char * x = (char *)malloc(len * sizeof(char));
    for (int i = 0; i < len; i++)
    {
        x[i] = n % 10;
        n /= 10;
    }
    for (int i = 0; i < len / 2; i++)
        if (x[i] != x[len - 1 - i])
            return 0;
    return 1;
}


int numLen(long int n)
{
    int x = 0;
    while (n != 0)
    {
        x++;
        n /= 10;
    }
    return x;
}