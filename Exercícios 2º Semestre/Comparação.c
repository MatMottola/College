#include <stdio.h>


int main() {
float n1,n2;
printf("Insira os números: \n");
scanf("%f %f",&n1,&n2);

(n1 == n2) 
	?  printf("Os números são iguais %.1f\n",n1)
	: (n1 > n2) 
		? printf("N1 = %.1f e maior que N2 = %.1f\n",n1,n2)
		: printf("N2 = %.1f e maior que N1 = %.1f\n",n2,n1);



    return 0;
}
