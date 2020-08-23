/*
 * palindrome(racecar) --> True 
 */
#include <stdio.h>
#include <string.h>

void reverse(char *str1,char *str2)
{
  int len1 = strlen(str1);
  int i,j;
  for (j = 0,i=len1 - 1; i >= 0; i--,j++)
  {
    str2[j] = str1[i];
  }
  str2[j] = '\0';

}

int palindrome(char str1[],char str2[])
{
  for (int i = 0; i < strlen(str1);i++)
  {
    if (str1[i] != str2[i])
      return 1;
  }
  return 0;
}

int main()
{
  char anotherword[] = "somebody once told me";
  char p_word[strlen(anotherword)+1];

  reverse(anotherword,p_word);
  if (palindrome(anotherword,p_word) == 1)
  {
    printf("%s is not a palindrome \n",anotherword);
  }
  else
  {
    printf("%s is a palindrome \n",anotherword);
  }

  return 0;
}
