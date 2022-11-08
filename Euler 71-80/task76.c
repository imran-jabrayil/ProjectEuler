#include <stdio.h>
#include <time.h>

int count = 0;

void calc(int number, int diff);

int main() {
    time_t start = time(NULL);

    int number = 100;
    int diff = 1;

    for (int i = 1; i < number; ++i)
        calc(number, i);

    printf("%d\n", count);
    printf("Time: %lf s.\n", difftime(time(NULL), start));

    return 0;
}

void calc(int number, int diff) {
    if (number - diff < 0)
        return;

    if (number - diff == 0) {
        ++count;
        return;
    } 

    number -= diff;
    for (int i = diff; i <= number; ++i)
        calc(number, i);
}
