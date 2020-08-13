#include <stdio.h>

int main()
{
  int arr[] = {9,4,8,5,6,8,9};
  int size = sizeof(arr) / sizeof(arr[0]);
  for (int x = 0; x < size; x++)
  {
    for (int y = 0; y < size - 1;y++)
      if (arr[y] > arr[y+1])
      {
        int temp = arr[y];
        arr[y] = arr[y+1];
        arr[y+1]= temp;
      }
  }

  for (int p = 0; p < size;p++)
  {
    printf("element %d = %d\n",p,arr[p]);
  }
  return 0;
}
