#include <stdio.h>
#include <math.h>

int main (void) {
float peso, altura, imc;
printf("Qual peso e altura?");
scanf("%f %f", &peso, &altura);
imc = peso/pow(altura,2);
printf("IMC = %.1f\n",imc);
if (imc<=30) printf("Nao este Obeso\n");
else printf("Obeso\n");

return 0;

}