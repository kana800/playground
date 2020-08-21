#include <stdio.h>
#include <string.h>

void string_reverse(char *s,int *p)
{
  int x = *p;
  while (x >= 0)
  {
    printf("%c",s[x]);
    x--;
  }
  printf("\n");
}

void string_reverse_m2(char *str)
{
  char *end = str + strlen(str) - 1;

  while (str < end)
  {
    char temp = *str;
    *str = *end;
    *end = temp;
    str++;
    end--;
  }
}

int main()
{
  char s[] = "This";
  char p[] = "That";
  int x = sizeof(s) / sizeof(s[0]);

  printf("Length of String is %d\n",s[x]);
  string_reverse(s,&x);
  string_reverse_m2(p);
  printf("%s\n",p);
  return 0;
}
