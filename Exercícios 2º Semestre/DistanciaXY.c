#include <stdio.h>
#include <math.h>

int main() {
   float xp,yp,xq,yq,dist = 0;
   
   printf("De as distancias dos pontos X:\n");
   printf("Ponto xP:");
   scanf("%f",&xp);
   printf("Ponto yP:");
   scanf("%f",&yp);
   
   printf("De as distancias dos pontos Q:\n");
   printf("Ponto xQ:");
   scanf("%f",&xq);
   printf("Ponto yQ:");
   scanf("%f",&yq);
   
   // Dif do ponto x e y | A² = (xp - xq) | B² = (yp-yq) | 
   
   dist = sqrt(pow(xp-xq,2) + pow(yp-yq,2));
   
   printf("A distancia entre P e Q: %.2f\n", dist);

    return 0;
}