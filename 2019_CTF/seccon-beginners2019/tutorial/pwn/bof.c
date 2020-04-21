#include <stdio.h>
#include <string.h>

char buffer[32];

int main(void) {
  char local[32];
  printf("hello\n");
  fgets(local, 128, stdin);
  strcpy(buffer, local);

  return 0;
}

