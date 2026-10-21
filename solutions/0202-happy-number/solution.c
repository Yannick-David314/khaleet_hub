#include <stdbool.h>

bool isHappy(int n) {
    int total = 0;
    while (n > 0) {
        total += pow(n % 10, 2);
        n = n / 10;               
    }
    if (total == 1) {
        return true;
    }
    else if (total == 4) {
        return false;
    }
    return isHappy(total);
}

