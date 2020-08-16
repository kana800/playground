#include <stdio.h>


void PrintArray(int *arr, int *size)
{
  for (int i = 0; i < *size;i++) {
    printf("element %d = %d\n",i,arr[i]);
  }
}


int main()
{
  int arr[] = {4,5,9,8,4,6,2,4};
  int size = sizeof(arr)/sizeof(arr[0]);

  for (int i = 0; i < size - 2;i++)
  {
    int min = i;
    for (int k = i+1; k < size ;k++)
    {
      if (arr[k] < arr[min])
      {
        min = k;
      }
    }
    int temp = arr[i];
    arr[i] = arr[min];
    arr[min] = temp;
  }

  PrintArray(arr, &size);
  return 0;
}
