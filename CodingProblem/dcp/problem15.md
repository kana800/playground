This problem was asked by Facebook.

Given a stream of elements too large to store in memory, pick a random element from the stream with uniform probability.

---

since the elements are too large to store in memory we are going to process the elements instead of storing them in a list. We can use a loop to select the random element


if the length of stream is known,
```python
from random import randint

def pickrandomelement(stream):
	return stream[randint(0,len(stream))]
```

if the length of stream is unknown.

```python
from random import randint

global count

def pickrandomelement(element):
	global count
	randomelement = None
	
	# number of elements encountered in the stream
	# can use enumerate instead
	count = 0

	# incremenet count
	count += 1

	if count == 1:
		randomelement = element
	else:
		i = randint(0, count - 1)
		if i == count - 1
			randomelement = element
	return randomelement

for index, element in enumerate(stream):
	randomelement = pickrandomelement(element)
	print(f"{random element}")

```

#### Resources 

- [video abour reservoir sampling](https://www.youtube.com/watch?v=Ybra0uGEkpM)
