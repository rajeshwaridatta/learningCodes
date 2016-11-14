#include<stdio.h>

int main() {
  int count;
  scanf("%d", &count);
  int sum = 0;
  while (count > 0) {
    int number;
    scanf("%d", &number);
    sum = sum + number;
    count = count - 1;
  }

  printf("%d", sum);
  return 0;
}
