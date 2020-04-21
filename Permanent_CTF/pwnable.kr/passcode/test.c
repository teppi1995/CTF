#include <stdio.h>

int main(void)
{
  int num;
  printf("scanf:");
  scanf("%d", num);

  printf("%x, %d\n", num, num);

  return 0;
}
