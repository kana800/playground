#include <stdio.h>


int main()
{

  int n = 10;
  int prime[n];
  int sum = 0;
  // creating an array with True Values
  for (int i =0; i < n+1;i++)
  {
    prime[i] = 0;
  }

  for (int p = 2; p *p <=n;p++)
  {
    if (prime[p] == 0)
    {
      for (int i = p*p;i<=n;i+=p)
      {
        prime[i] = p;
      }
    }
  }

  for (int p = 2;p <= n;p++)
  {
    if (prime[p]== 0)
    {
      printf("%d\n",p);
      sum += p;
    }
  }


  printf("sum = %d\n",sum);
  return 0;
}
