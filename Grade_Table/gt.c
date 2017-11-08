#include <stdio.h>
#include <stdlib.h>
  
int main() {

  for (int i = 1; i < 13; i++) {
    for (int j = 1; j < 13; j++) {
      printf(" %d", i*j);
    }
    printf("\n");
  }
  return 0;

}
