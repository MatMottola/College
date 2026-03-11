#include <math.h>
#include <stdio.h>

int main(void) {
int x,n,r;

printf("De a base X\n");
scanf("%d",&x);

printf("De a expoente N\n");
scanf("%d",&n);

for(int i=0; i <= n; i++){
    r = pow(x,i);
    printf("Potencia de %d^%d = %d\n",x,i,r);
    }
return 0;

}