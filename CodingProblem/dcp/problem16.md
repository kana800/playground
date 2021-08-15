This problem was asked by Twitter.

You run an e-commerce website and want to record the last N order ids in a log. Implement a data structure to accomplish this, with the following API:

record(order_id): adds the order_id to the log get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N. You should be as efficient with time and space as possible.

---

Assuming that the size of the log is predefined, we can implement a simple double linked list as the data structure that imitates `FILO` behaviour, the first record included will be the record that removed at last (if the size is full). If we exceed the size of the log we need to copy the current log without the first element i.e (in python)
```python
if len(log) > size:
	# creating a new log
	log = log[1:].copy()
```

`get_last(i)` can be implemented by counting elements from the last value. If we are using C, we can have a pointer to the last element of the array and move according the `ith` index.

```c

// storing the head and the tail
struct node *head = NULL;
struct node *tail = NULL;
int size = 0;
int currentlengthlog = 0;

// structure
struct node {
	int order_id;
	struct node* nextPtr;
	struct node* lastPtr;
}

// creates a log
int * createOrder(int order_id){
	int* temp = (int *)malloc(sizeof(struct node));
	temp->order_id = order_id;
	head->nextPtr = NULL;
	head->lastPtr = NULL;
	return temp;
}

// records the element
void record(int order_id){
	struct node * tempnode = createOrder(order_id)
	// checking if the list is empty
	if ((head == NULL) && (tail == NULL)){
		head = tempnode;	
		tail = tempnode;
		// incrementing the size
		currentlengthlog += 1;
	}
	// checking if the log exceeds the given size
	if (currentlengthlog > size){
		// deleting the last node
		struct node * temp = tail->lastPtr;
		free(tail);
		// changing the new nodes ptr
		tempnode->lastptr = temp;
		// new tail
		tail = tempnode;
	}else{
		// insert at the head
		struct node * temp = head;
		tempnode->nextPtr = temp;
		// changing heads
		head = tempnode;
	}
}		
```


If using python, we can use a `Class`

```python
class Log:
	def __init__(self, size):
		"""
		size -> size of the log
		"""
		self.log = list()
		self.size = size

	def record(self, order_id):
		self.log.append(order_id)
		# check if the size is exceed
		if len(self.log) > self.size:
			self.log = self.log[1:].copy()


	def get_last(self, i):
		return self.log[-i]

```


for `c` implementation,
	- time complexity for `record` would be `O(1)` because we arent iterating through and array
	- time complexity for `get_last` would be `O(n)`

for `python` implementation,
	- time complexity for `record` would be `O(n)` because we are copying another list to another list
	- time complexity for `get_last` would be `O(1)` because its a look up.
