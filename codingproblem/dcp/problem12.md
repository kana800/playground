This problem was asked by Amazon.

There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time. Given N, write a function that returns the number of unique ways you can climb the staircase. The order of the steps matters.

For example, if N is 4, then there are 5 unique ways:
```
1, 1, 1, 1
2, 1, 1
1, 2, 1
1, 1, 2
2, 2
```
What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of positive integers X? For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.

---

Find the number of possible ways that the sum of the generated numbers add up to `N`. we can use recursion to solve this problem.

Example:
```
when n = 1 ---> [1]
when n = 2 ---> [1,1] [2]
when n = 3 ---> [1,1,1] [1,2] [2,1]
when n = 4 ---> [1,1,1,1] [2,1,1] [1,2,1] [1,1,2] [2,2]
```

The pattern seems to be life the fibonacci sequence, whe ccan say to get the third step we have to go the first step and then go steps up and to go the fourth step you can go the third step and go one more step or go the second step and move two steps.
```
s(3) = s(2) + s(1)
s(4) = s(3) + s(2)
```

[Implementation in Python](codes/problem12.py)

Time complexity: `O(|stepsize|^N)` exponential growth, we can use dynamic programming to speed things up.

[resources](https://www.dailycodingproblem.com/blog/staircase-problem/)
