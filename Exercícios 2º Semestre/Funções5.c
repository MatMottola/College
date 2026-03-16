#include <stdio.h>
#include <math.h>

float raiz(float x) {
float r = x / 2.0;
    
while (fabs(r*r - x) >= 0.001)
    {
        r = (r*r + x) / (2*r);
    }
    return r;
}



int main () {
float x;
    
printf("Digite um numero valido: \n");
scanf("%f",&x);

if(x<0)  printf("Numero invalido");

else  printf("Raiz aproximada:\n%.3f",raiz(x));

     return 0;
}