// converts binary number to a decimal number

#include <stdio.h>

int BinaryToDecimal(int binary)
{
  int n =  binary;
  int decimal = 0;
  int base = 1;
  int last_digit = 0;

  while (n != 0)
  {
    last_digit = n % 10 ;
    decimal += last_digit * base;
    base *= 2;
    n /= 10;
  }

  return decimal;
}

int main()
{
  int x = BinaryToDecimal(10000);
  printf("Binary Number is %d\n",x);
  return 0;
}
