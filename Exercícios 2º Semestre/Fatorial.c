#include <stdio.h>

int main(void) {

int x;
int fat = 1;

printf("De o numero\n");
scanf("%d",&x);

for(int i = 1; i<= x; i++){
    fat *=i;
        }
printf("O Fatorial de %d! = %d\n",x,fat);
return 0;
}