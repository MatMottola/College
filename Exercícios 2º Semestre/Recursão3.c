#include <stdio.h>

void CountP(int n) {
if( n==0 ) return;
CountP(n-1);
printf("%d\n",n);

}

int main(void) {
int n;

printf("Num? ");
scanf("%d",&n);
CountP(n);

return 0;

}