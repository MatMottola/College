#include <stdio.h>

int main() {
   float q, l = 0;
    printf("Insira a distancia em Kilometros: ");
    scanf("%f", &q);
    printf("Insira o total de litros gastos: ");
    scanf("%f", &l);
    
    float t = q/l;
    
    printf("O consumo medio e de: %.2f",t);

    return 0;
}