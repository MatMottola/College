#include <stdio.h>
#include <math.h>

int main() {
float x,y;
char o;

printf("Expressao? \n");
scanf("%f %c %f", &x,&o,&y);

    switch(o) 
         {
        case '+': printf("Resultado = %.2f\n",x+y);
        break;
        
        case '-': printf("Resultado = %.2f\n",x-y);
        break;
        
        case 'x':;
        case '*': printf("Resultado = %.2f\n",x*y);
        break;
        
        case ':':;
        case '/' : 
            if(y==0) printf("Erro devido a divisão com zero!");
            else printf("Resultado = %.2f\n",x/y);
        break;
        
        default : printf("Operador Invalido\n");
        break;
        }
    
return 0;
}