Problem 2
---------
This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?

#### option #1

we can get the product of all the elements in the array, using a for-loop and use division

##### counter examples? 

will not work with negative number because of the signs, for example `[-1, 2 ,-3 ,-4, 5]`. The product of every element would be `-1 * 2 * -3 * -4 * -5 = -120`. 
If we divide product of every element with the element at the index. `[-120/-1,-120/2,-120/-3,-120/-4,-120/5]` we will get `[120,-60,40,30,-24]` 

```c
int productofeveryelement(int *arr, int size){
	int sum = 0;
	for( int i =0 ;i < n; i++){
		sum *= arr[i];	
	}
	return sum;
}

int * newarray(int *arr, int size){
	// finding the sum
	int sum = productofeveryelement(arr, size);
	// new array
	int narr[size];
	// loop through the array
	for (int i = 0; i < n; i++){
		narr[i] = sum / arr[i];
	}
	return narr;
}
```

Big Oh -> `O(n)`
