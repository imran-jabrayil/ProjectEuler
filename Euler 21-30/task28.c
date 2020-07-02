#include <stdio.h>
#include <stdlib.h>


long int findSum(long int * A, int size);
void fillMatrix(long int * A, int size);


int main()
{
    int size;
    printf("Enter the side of your matrix: ");
    scanf("%d", &size);
    long int * matrix = (long int *)calloc(size * size, sizeof(long int));
    fillMatrix(matrix, size);
    long int sum = findSum(matrix, size);
    printf("%ld\n", sum);
    return 0;
}


long int findSum(long int * A, int size)
{
    long int sum = -1;
    for (int i = 0; i < size; i++)
        sum += A[i * size + i] + A[(size - 1 - i) * size + i];
    return sum;
}


void fillMatrix(long int * A, int size)
{
    int x = size / 2, y = size / 2;
    int step = 0;
    long int num = 1;
    A[x * size + y] = 1;
    while (!(x == 0 && y == 0))
    {
        step++;
        if (step % 2 == 0)
        {
            for (int i = 0; i < step; i++)
            {
                y--; num++;
                A[x * size + y] = num;
            }
            for (int i = 0; i < step; i++)
            {
                x--; num++;
                A[x * size + y] = num;
            }
        }
        else 
        {
            for (int i = 0; i < step; i++)
            {
                y++; num++;
                A[x * size + y] = num;
            }
            for (int i = 0; i < step; i++)
            {
                x++; num++;
                A[x * size + y] = num;
            }
        }
    }
    for (int i = 1; i < size; i++)
    {
        num++;
        A[i] = num;
    }
}