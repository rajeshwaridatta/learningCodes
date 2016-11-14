#include<stdio.h>

int main() {
  int count;
  scanf("%d", &count);
  int position = 0;
  while (count > 0) {
    int number;
    scanf("%d", &number);
    position=position +1;
    if(number == 0){
      break;
    }
    count = count - 1;
  }

  printf("%d", position);
  return 0;
}
