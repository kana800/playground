Problem 4
---------
This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input `[3, 4, -1, 1]` should give `2`. The input `[1, 2, 0]` should give 3.

You can modify the input array in-place.


#### Option #1

We can use `set`, create a set in that range of the minimum number to maximum number and find the missing intersection values.

```python
a = [3,4,-1,1]
minnumber = min(a)
maxnumber = max(a)
b = [i for i in range(minnumber, maxnumber)]
missing_numbers = b - a.intersection(b)
```

#### Option #2

[code implementation](codes/problem4.c)
