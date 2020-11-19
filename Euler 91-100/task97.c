#include <stdio.h>
#include <time.h>


long int calculate();


int main() 
{
    time_t start = time(NULL);
    printf("%ld\n", calculate());
    printf("Time: %lf s.\n", difftime(time(NULL), start));
    return 0;
}


long int calculate() 
{
    long int power = 7830457, ostatok = 10000000000, num = 1;
    for (long int i = 0; i < power; i++) 
    {
        num = num * 2 % ostatok;
    }
    return (num * 28433 + 1) % ostatok;
    
}