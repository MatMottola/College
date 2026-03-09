#include <stdio.h>  
#include <conio.h>



int main() {
float p1,p2,m;
int faltas;
printf("Insira as notas: \n");
scanf("%f %f",&p1,&p2);

printf("Insira o numero de faltas: \n");
scanf("%d",&faltas);


m = (p1 + p2)/2;


if (m>=6 && faltas <= 5)  {
            _textcolor(9);
            puts ("Aprovado ");
          }    
else        {
            _textcolor(12);
            puts ("Reprovado ");
            }
	_textcolor(7);
    return 0;
}