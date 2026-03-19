#include <stdio.h>

int par(int n){
    if (n == 0) return 1;
    if (n == 1) return 0;
    return par(n-2);
    }


int main (){
    
int n;

printf("Num? ");
scanf("%d",&n);
if (par(n)) printf("Par");
else printf("Impar");
return 0;
}