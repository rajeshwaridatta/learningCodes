#include<stdio.h>

int main() {
  while(1) {
    float fahrenheit = 0;
    scanf("%f", &fahrenheit);
    if (fahrenheit == 0)
      break;
    float centigrade = ((fahrenheit - 32) / 9)*5;
    printf("%f\n", centigrade);
  }
  
  return 0;
}
