#include <stdio.h>


int isRightAngled(int a, int b, int c);
int countSolutions(int perimeter);


int main()
{
    int x, solut = 0;
    int temp;
    for (int p = 1; p <= 1000; p++)
    {
        temp = countSolutions(p);
        if (temp > solut)
        {
            solut = temp;
            x = p;
        }
    }
    printf("%d\n", x);
    return 0;
}


int isRightAngled(int a, int b, int c)
{
    if (a * a + b * b == c * c)
        return 1;
    return 0;
}


int countSolutions(int perimeter)
{
    int count = 0;
    for (int i = 1; i < perimeter; i++)
        for (int j = 1; j < i; j++)
            if (isRightAngled(i, j, perimeter - i - j))
                count++;
            else if (i + j > perimeter)
                break;
    return count;
}