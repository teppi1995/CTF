#include <stdio.h>

char * func(char *str, int len, int key){
  int i = 0;

  while(i < len) {
    str[i] = str[i] ^ key;
    i++;
  }
  return str;
} 

int main(void) {
  char a[] = "hi bob";
  printf("%s\n", func(a, 6, 0x20));
  return 0;
}

