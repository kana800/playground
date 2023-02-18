This problem was asked by Amazon.

Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.

For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".

---

#### method #1

we can have a two pointer,
```
abcba
^ (start)
^ (end)
```
we will move the `end` pointer until we have k distinct characters and store the length of substring plus its index in a dictionary
```
length = end - start + 1
```

Time Complexity: `O(n)`

[Solution to Problem #13](codes/problem13.py)
