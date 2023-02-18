Problem 1
---------

Given a list of numbers, return whether any two sums to k. For example, given `[10, 15, 3, 7]` and `k` of `17`, return true since `10 + 7` is `17`.

Bonus: Can you do this in one pass?

#### option #1

we can calculate the value for each element of the array by adding it against every other element. For example: In the array `[10,5,3,7]`, if we take the first element of the array: `10`, we can add it against every other element, `10 + 5`, `10 + 3` and `10 + 7` and once we find the value `k`. we can return **true**.

##### counter examples? 

None

We are doing **Exhaustive Search** and we need to iterate through the array two times!. Big Oh for the following scenario, would be `O(n ^ 2)`.

```python
def checkKpresent(arr, k):
	for i in arr:
		for j in arr:
			if i+j == k:
				return True
	return False
```

#### option #2

we can iterate through the array and substract value `k` from the array, for example: Lets take an empty array,`P`, we will iterate through the array `[10,15,3,7]` (`k = 17`), we will take the first index and substract `k` from `10` and add that value to the array`P` and once we move to `7`, we will check if that value is in `P`, if so, we have found the answer.

```python
def checkKpresent(arr, k):
	P = set()
	# iterate through the array
	for num in arr:
		# check if the value is present
		if num in P:
			return True
		else:
			P.add(K - num)
	return False
```

why `P = set()`, because we need to makesure the same value is not added twice
