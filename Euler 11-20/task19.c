#include <stdio.h>
#include <math.h>


int weekday(int d, int m, int y, int c);
int leapCheck(int year);

const int days_in_months[13] = {
    0, 31, 28, 31, 30, 31, 30,
    31, 31, 30, 31, 30, 31
};


int main()
{
    int year = 1901, day = 1, month = 1;
    int count = 0;
    while (!(day == 1 && month == 1 && year == 2001)) {
        if (weekday(day, month, year % 100, year / 100) == 0 && day == 1)
            count++;
        if (day == days_in_months[month] && month == 12)
        {
            year++;
            day = 1;
            month = 1;
        }
        else if (day == days_in_months[month])
        {
            day = 1;
            month++;
        }
        else 
            day++;
    }
    printf("%d\n", count);
    return 0;
}


int weekday(int d, int m, int y, int c)
{
    if (m <= 2)
        m += 10;
    else 
        m -= 2;
    int x = (d + floor(2.6 * m - 0.2) + y + floor(0.25 * y) + floor(0.25 * c) - 2 * c);
    x = x % 7;
    if (x < 0)
        x += 7;
    return x;
}


int leapCheck(int year)
{
    if (year % 4 != 0)
        return 0;
    else if (year % 100 != 0)
        return 1;
    else if (year % 400 != 0)
        return 0;
    else
        return 1;
}