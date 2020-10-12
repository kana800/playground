#include <stdio.h>

int partition(int* A,int start,int end)
{
  int pivot = A[end];
  int pIndex = start; // partition index
  int temp;
  for (int i = start; i<end ; i++ )
  {
    if (A[i] <= pivot)
    {
      temp = A[i];
      A[i] = A[pIndex];
      A[pIndex]=temp;
      pIndex += 1;
    }
  }
  temp = A[pIndex];
  A[pIndex] = A[end];
  A[end]=temp;
  return pIndex;
}


void quicksort(int* A,int start, int end)
{
  int pIndex;
  if (start < end)
  {
    pIndex = partition(A, start, end);
    quicksort(A, start, pIndex -1);
    quicksort(A, pIndex +1 , end);
  }

}

int main()
{
  int A[] = {7,2,1,6,8,5,3,4};
  int size = sizeof(A)/sizeof(A[0]);
  quicksort(A,0,7);
  
  for (int i = 0; i < size;i++)
  {
    printf("element %d = %d\n",i,A[i]);
  }

  return 0;
}
