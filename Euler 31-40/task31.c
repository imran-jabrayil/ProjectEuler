#include <stdio.h>
#include <time.h>


int main()
{
    time_t start = time(NULL);
    int count = 0;
    for (int i = 0; i <= 200; i++)
        for (int j = 0; j <= 100; j++)
            for (int k = 0; k <= 40; k++)
                for (int l = 0; l <= 20; l++)
                    for (int m = 0; m <= 10; m++)
                        for (int n = 0; n <= 4; n++)
                            for (int o = 0; o <= 2; o++)
                                for (int p = 0; p <= 1; p++)
                                    if (i * 1 + j * 2 + k * 5 + l * 10 + m * 20 + n * 50 + o * 100 + p * 200 == 200)
                                        count++; 
    printf("%d\n", count);
    printf("Time: %lf s.\n", difftime(time(NULL), start));
    return 0;
}