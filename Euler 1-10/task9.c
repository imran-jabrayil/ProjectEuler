#include <stdio.h>


int main()
{
    for (long int a = 1; a < 1000; a++)
        for (long int b = 1; b < 1000; b++)
            for (long int c = 1; c < 1000; c++)
                if ((a*a + b*b == c*c) && (a + b + c == 1000))
                {
                    printf("%ld\n", a*b*c);
                    return 0;
                }
    return 0;
}