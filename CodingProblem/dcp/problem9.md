This problem was asked by Airbnb.

Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 8] should return 12, since we pick 4 and 8. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

---

```python
def largest_none_adjacent_sum(arr):
    prev = 0 # previous number
    larg = 0 # maximum number
    for i in arr:
        #tempLarg = max(prev, larg)
  		#prev = larg + i
        #larg = tempLarg
    	prev,larg = larg, max(larg, perv + i)
    #return max(larg, prev)
    return larg
```

Time complexity : `O(n)` because we are iterating through the array only once.