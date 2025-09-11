#include <stdio.h>

int main() {
    long long sum = 0;
    int a = 1, b = 2, next;

    while (b <= 4000000) {
        if (b % 2 == 0) {
            sum += b;  // add even term
        }
        next = a + b; // generate next Fibonacci number
        a = b;
        b = next;
    }

    printf("Sum of even Fibonacci numbers %lld\n", sum);
    return 0;
}
