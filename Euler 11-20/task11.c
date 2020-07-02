#include <stdio.h>


typedef int matrix[20][20];
long int vert(matrix a, int row, int col);
long int horiz(matrix a, int row, int col);
long int diag1(matrix a, int row, int col);
long int diag2(matrix a, int row, int col);


int main()
{
    matrix grid;
    long int prod = 0, temp;
    for (int i = 0; i < 20; i++)
        for (int j = 0; j < 20; j++)
            scanf("%d", &grid[i][j]);
    for (int i = 0; i < 17; i++)
        for (int j = 0; j < 20; j++)
        {
            temp = vert(grid, i, j);
            if (temp > prod)
                prod = temp;
        }
    for (int i = 0; i < 20; i++)
        for (int j = 0; j < 17; j++)
        {
            temp = horiz(grid, i, j);
            if (temp > prod)
                prod = temp;
        }
    for (int i = 0; i < 17; i++)
        for (int j = 0; j < 17; j++)
        {
            temp = diag1(grid, i, j);
            if (temp > prod)
                prod = temp;
        }
    for (int i = 0; i < 17; i++)
        for (int j = 3; j < 20; j++)
        {
            temp = diag2(grid, i, j);
            if (temp > prod)
                prod = temp;
        }
    printf("%ld", prod);
    return 0;
}   




long int vert(matrix a, int row, int col)
{
    return a[row][col] * a[row + 1][col] * a[row + 2][col] * a[row + 3][col];
}

long int horiz(matrix a, int row, int col)
{
    return a[row][col] * a[row][col + 1] * a[row][col + 2] * a[row][col + 3];
}

long int diag1(matrix a, int row, int col)
{
    return a[row][col] * a[row + 1][col + 1] * a[row + 2][col + 2] * a[row + 3][col + 3];
}

long int diag2(matrix a, int row, int col)
{
    return a[row][col] * a[row + 1][col - 1] * a[row + 2][col - 2] * a[row + 3][col - 3];
}