#include <stdio.h>
#include <math.h>

int main() {
int a,b,c;
float r1,r2;

printf("Insira o valor de A\n");
scanf("%d",&a);

if (a == 0) {
     printf("Valor de A necessita ser diferente de 0");
     return 0;
            }
printf("Insira o valor de B\n");
scanf("%d",&b);
printf("Insira o valor de C\n");
scanf("%d",&c);

r1 = (-b + sqrt(pow(b,2)-4*a*c)) / (2*a);
r2 = (-b - sqrt(pow(b,2)-4*a*c)) / (2*a);

printf("As raizes sao:\nR1 = %.2f \nR2 = %.2f \n",r1,r2);

    return 0;
}
