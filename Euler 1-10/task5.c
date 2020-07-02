#include <stdio.h>


int isDiv(int n);


int main()
{
    int x = 1;
    while (x)
    {
        if (isDiv(x))
        {
            printf("%d\n", x);
            return 0;
        }
        else 
            x++;
    }
    return 0;
}


int isDiv(int n)
{
    for (int i = 1; i <= 20; i++)
        if (n % i != 0)
            return 0;
    return 1;
}