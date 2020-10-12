#include <stdio.h>

void merge(int arr[],int left,int mid,int right)
{
  
  
  int leftpart[(mid+1)-left];
  int rightpart[(right+1)-(mid+1)];
  
  // initializing left  array
  
  for (int i = left;i < mid + 1;i++)
  {
    leftpart[i] = arr[i];
  }

  // initializing right array
  for (int i = mid+1;i < right + 1;i++)
  {
    rightpart[i] = arr[i];
  }

  //size of leftpart
  int s_left_part = sizeof(leftpart)/sizeof(leftpart[0]); 
  //size of rightpart
  int s_right_part = sizeof(rightpart)/sizeof(rightpart[0]); 

  int leftindex = 0;
  int rightindex = 0;
  
  for (int i = left;i < right + 1;i++)
  {
    if (s_left_part > leftindex && s_right_part > rightindex)
    {
      if (leftpart[leftindex] > rightpart[rightindex])
      {
        arr[i] = rightpart[rightindex];
        rightindex += 1;
      }
      else
      {
        arr[i] = leftpart[leftindex];
        leftindex += 1;
      }
    }
    else if (s_left_part > leftindex) 
    {
     arr[i] = leftpart[leftindex]; 
     leftindex+= 1 ;
    }
    else
    {
     arr[i] = rightpart[rightindex]; 
     rightindex+= 1 ;
    }
  }
}

void merge_sort_algorithm(int arr[],int left,int right)
{
  if (left < right)
  {
    int mid = (left + right) /2;
    merge_sort_algorithm(arr, left,mid);
    merge_sort_algorithm(arr, mid+1,right);
    merge(arr,left,mid,right);
  }
}


int main()
{
  int arr[] = {9,6,4,8,6,9};
  int size = sizeof(arr) / sizeof(arr[0]);
  
  merge_sort_algorithm(arr,0,size -1);
  
  for (int k = 0; k < size;k++)
  {
    printf("arr %d = %d\n",k,arr[k]);
  }

  return 0;
}
