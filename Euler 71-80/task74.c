#include <stdio.h>

typedef unsigned uint;
typedef unsigned long long ull;

ull factorials[10];
void generateFactorials();
ull getFactorial(uint digit);
ull getNextTerm(ull number);
int getChainCount(ull number);


int main() {
    generateFactorials();
    
    // int count = getChainCount(540);
    // printf("%d\n", count);

    ull limit = 1000000;
    int counter = 0;

    for (ull i = 1; i < limit; ++i)
        if (getChainCount(i) == 60)
            ++counter;
    
    printf("Result: %d\n", counter);
    return 0;
}

void generateFactorials() {
    ull product = 1;
    factorials[0] = 1;
    for (int i = 1; i <= 9; ++i) {
        product *= i;
        factorials[i] = product;
    }
}

ull getFactorial(uint digit) {
    return factorials[digit];
}

ull getNextTerm(ull number) {
    ull sum = 0;
    
    while (number) {
        sum += getFactorial(number % 10);
        number /= 10;
    }

    return sum;
}

int getChainCount(ull number) {
    int count = 0;
    ull terms[61];

    terms[count++] = number;

    ull term;
    while (count < 61) {
        term = getNextTerm(terms[count - 1]);

         for (int i = 0; i < count; ++i)
            if (terms[i] == term)
                return count;
        
        terms[count++] = term;
    }

    return count;
}
