#include<stdio.h>
int main() {
int n, se,so, subtract;
int count=0;
scanf("%d", &count);
while( count>0){
  scanf("%d", &n);
  if (n % 2==0){
    se=se+n;
  } else{
    so=so+n;
  }
  subtract= se-so;
}
printf("%d",subtract);

  return 0;
}
