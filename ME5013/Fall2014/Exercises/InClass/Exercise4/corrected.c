#include <stdio.h>
#include <errno.h>
void quit(char *message) {
  printf("Error number %d\n ", errno);
  exit(1);
}
