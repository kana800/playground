This problem was asked by Facebook.

Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.

---

This is recursive problem, check the number of ways you can spilt the message using a recursion tree.

```
message: 101 -> [10,1]
message: 2626 -> [2,6,2,6] [26,26] 
message: 123 -> [1,2,3] [12,3] [1,23]
message: 123456789 -> [1,2,3,4,5,6,7,8,9] [12,3,4,5,6,7,8,9]
```

[Implementation of problem #7(recursive)](codes/problem7.py)

If we use memoization we can improve the speed of the algorithm.
