#include <stdio.h>

double potencia(double x,unsigned int n) {
double p = 1;
for(unsigned int i=1; i<=n; i++)
    { 
    p = p * x;
    }


return p;

}
int main(void) {
printf("%.1f\n",potencia(2,5)); 
return 0;
}