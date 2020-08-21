#include <stdio.h>

int main()
{
  char *test_string = "the quick brown fox jumped over the fence"; // test string
  // vowel counters
  int a_counter = 0;
  int e_counter = 0;
  int i_counter = 0;
  int o_counter = 0;
  int u_counter = 0;

  for (int i = 0; test_string[i] != '\0';i++)
  {
    char letter = test_string[i];
    switch (letter)
    {
      case 'a':
      case 'A':
        a_counter+=1;
        break;
      case 'e':
      case 'E':
        e_counter+=1;
        break;
      case 'o':
      case 'O':
        o_counter+=1;
        break;
      case 'i':
      case 'I':
        i_counter+=1;
        break;
      case 'u':
      case 'U':
        u_counter+=1;
        break;
    }
  }
  printf("String = %s\n\tconsists of a = %d , e = %d, i = %d, o = %d, u = %d\n",test_string,a_counter,e_counter,i_counter,o_counter,u_counter);
  return 0;

}
