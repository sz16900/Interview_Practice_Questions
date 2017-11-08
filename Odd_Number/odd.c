#include <stdio.h>
#include <stdlib.h>

int main () {
  for (int i = 1; i < 100; i = i+2) {
    printf("%d ", i);
  }
  printf("\n");
  return 0;
}
