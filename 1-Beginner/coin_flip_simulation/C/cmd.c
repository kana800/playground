#include <stdio.h>
#include <stdlib.h>


int main()
{
  int n = 0;
  int tails = 0; // [0] number of times tails come up
  int heads = 0; // [1] number of times heads come up

  printf("Enter the Number of Turns\n");
  scanf("%d",&n);

  while (n > 0)
  {
    int r = rand() % 2;
    if (r == 0)
    {
      tails += 1;
    }
    else if (r == 1)
    {
      heads += 1;
    }
    n -= 1;
  }

  printf("Heads = %d \nTails = %d \n",heads,tails);
  return 0;
}
