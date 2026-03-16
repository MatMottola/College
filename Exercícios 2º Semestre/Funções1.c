#include <stdio.h>
void g(void) { 
    puts("G"); 
    
}

void f(void) { 
    puts("F1"); g(); puts("F2");
    }
int main(void) {
    puts("M1"); 
    f(); puts("M2"); 
    return 0; 
    
}