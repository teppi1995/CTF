#include <stdio.h>

int inc(int a)
{
  return --a;
}
  
int main()
{
  return inc(10);
}

