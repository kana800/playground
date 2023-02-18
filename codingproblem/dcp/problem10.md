This problem was asked by Apple.

Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.

---

we can use the `sleep` from `time` module

```python
from time import sleep

def testFunction():
	return "Hello World!"

def jobScheduler(f, n):
	"""
	f -> function
	n -> time in milliseconds
	calls the function after n milliseconds
	"""
	sleep(n)
	testFunction()
```


References
- [link](https://www.youtube.com/watch?v=Gs5jGDROx1M)
