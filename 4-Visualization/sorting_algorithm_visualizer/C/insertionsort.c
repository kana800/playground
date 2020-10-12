#include <stdio.h>

void Printer(int arr[],int *size)
{
  for (int i = 0 ; i < *size ; i++)
  {
    printf("element %d = %d\n",i,arr[i]);
  }
}


int main()
{
  int arr[] = {9,4,8,6,5,4};
  int size = sizeof(arr)/sizeof(arr[0]);

  for (int i = 1; i < size; i++)
  {
    int value = arr[i];
    int hole = i; // index
    while (hole > 0 && arr[hole -1 ] > value)
    {
      arr[hole] = arr[hole - 1];
      hole -= 1;
    }
    arr[hole] = value;
  }

  // printing the array
  Printer(arr,&size);
  return 0;
}
