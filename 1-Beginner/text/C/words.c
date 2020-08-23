#include <stdio.h>
#include <string.h>

int word_counter(char * str1)
{
  int space_counter = 0;
  for (int i =0;i < strlen(str1);i++)
  {
    if (str1[i] == ' ')
    {
      space_counter += 1;
    }
  }
  return space_counter + 1;
}


int main()
{
  char *str1 = "This is a test string lets add another word";
  
  int word = word_counter(str1);
  printf("%s \n %d words\n", str1,word);
  return 0;
}
