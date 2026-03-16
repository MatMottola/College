#include <stdio.h>
void f(void); 

void g(void); 

int main(void) {
    puts("M1");
    f();
    puts("M2"); 
    
    return 0; }
    
void f(void) { 
    puts("F1");
    g();
    puts("F2");
    }
void g(void) { 
    puts("G"); 
    
}