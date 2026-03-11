#include <stdio.h>

int main() {
int x=5,y, z;

y = ++x + 2;
z = x-- + 2;

printf("x=%d y=%d z=%d\n",x,y,z); // x=5 y=8 z=8

return 0;
}