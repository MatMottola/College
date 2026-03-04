#include <stdio.h>

int main() {
    float f = 0;
    float c = 0;
    
   printf("Qual a temperatura em Fahrenheit");
   scanf("%f",&f);
   
   c = (f-32) * (5.0/9.0);
   
   printf("%.2f\n",c);

    return 0;
}