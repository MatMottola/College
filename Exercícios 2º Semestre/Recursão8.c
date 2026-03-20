#include <stdio.h>


int q(int n){
    if (n==0) return 1;
    if (n==1) return n;
    return (2 * n-1) + q(n-1);
}

int main(void) {

int n;

printf("Quadrado do Num? ");
scanf("%d",&n);
printf("Quadrado: %d\n",q(n));

return 0;

}