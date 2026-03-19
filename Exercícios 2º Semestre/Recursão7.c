#include <stdio.h>

int prod(int m,int n){
   if (n == 0 || m == 0) return 0;
    return m + prod(m,n-1);
   
   
    }


int main(void) {
    int m, n;
    
    printf("Primeiro Num? ");
    scanf("%d", &m);
    printf("Segundo Num? ");
    scanf("%d", &n);
    
    printf("%d x %d = %d\n", m, n, prod(m, n));
    return 0;
}